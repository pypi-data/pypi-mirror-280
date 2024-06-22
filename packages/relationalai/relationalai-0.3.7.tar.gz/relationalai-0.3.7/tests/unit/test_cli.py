# ---------------------------------------------------------------
# Test the RAI CLI commands
# ---------------------------------------------------------------

import sys
import rich
import pytest
from io import StringIO
from unittest.mock import patch
from click.testing import CliRunner
from relationalai.clients import config
from relationalai.clients.config import ConfigStore
from tests.unit.test_cli_mocks import (
    az_profile,
    sf_profile,
    mocked_engines_list,
    mocked_imports_status,
    mocked_txns_list_azure,
    mocked_txns_list_snowflake,
    mocked_imports_get_details,
    mocked_list_imports_response,
    mocked_import_stream_response
)

# ---------------------------------------------------------------
# Setup
# ---------------------------------------------------------------

rich.reconfigure(file=StringIO(), width=120)

# ---------------------------------------------------------------
# Util
# ---------------------------------------------------------------
class RunnerResult:
    def __init__(self, output, exit_code):
        self.output = output
        self.exit_code = exit_code

def run_command(cli_command, *args):
    runner = CliRunner()
    result = runner.invoke(cli_command, *args)
    console = rich.get_console()
    str_output = console.file.getvalue()
    console.file.truncate(0)
    return RunnerResult(str_output, result.exit_code)

# ---------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------

@pytest.fixture(autouse=True)
def run_before_each_test(mocker):
    # Mock get_config before each test so we can deal with the ensure_config
    gs_instance = mocker.patch('relationalai.tools.cli_helpers.get_config').return_value
    gs_instance.get.file_path = "some path"

    yield

    # Cleanup
    mocker.stopall()

# ---------------------------------------------------------------
# rai config:check
# ---------------------------------------------------------------
def test_config_check(mocker):
    from relationalai.tools.cli import config_check
    engine_response = mocked_engines_list[4]

    mocker.stopall()

    cs = mocker.patch.object(ConfigStore, 'get')
    cs.return_value = None

    gfc = mocker.patch('relationalai.clients.config._get_full_config')
    gfc.return_value = sf_profile, "some path"

    # ---------------------------------------------------------------
    #  Engine/Prop not found
    # ---------------------------------------------------------------

    result = run_command(config_check)

    assert "Error: Missing config value for 'engine'" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Engine not found
    # ---------------------------------------------------------------

    sf_profile['engine'] = 'foo'

    instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    instance.get_engine.return_value = None

    result = run_command(config_check)

    assert "Error: Configured engine 'foo' not found" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Engine in wrong state
    # ---------------------------------------------------------------

    instance.get_engine.return_value = engine_response
    instance.is_valid_engine_state.return_value = False

    result = run_command(config_check)

    assert "Error: Engine 'foo' is in an invalid state: 'SUSPENDED'" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  All good
    # ---------------------------------------------------------------

    instance.is_valid_engine_state.return_value = True
    spy = mocker.spy(instance, 'get_engine')

    result = run_command(config_check)

    spy.assert_called_once_with('foo')
    assert "Connection successful!" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Exception handling
    # ---------------------------------------------------------------

    with patch('relationalai.tools.cli.get_resource_provider', side_effect=Exception('Provider Error')):
        result = run_command(config_check)

    assert "Error: Provider Error" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai profiles:switch
# ---------------------------------------------------------------
def test_profiles_switch(mocker):
    from relationalai.tools.cli import profile_switch

    # Setup mocks for the ConfigStore used throughout the test
    rv = {'sf': { "platform":"snowflake" }, 'az': { "platform":"azure" }}
    mocker.patch('relationalai.clients.config.ConfigStore.get_profiles', return_value = rv)
    mocker.patch('relationalai.clients.config.ConfigStore.change_active_profile', return_value = True)
    mocker.patch('relationalai.clients.config.ConfigStore.save', return_value = True)

    # ---------------------------------------------------------------
    #  Switch profile (non-interactive mode)
    # ---------------------------------------------------------------

    spy_profile = mocker.spy(ConfigStore, 'change_active_profile')
    spy_save = mocker.spy(ConfigStore, 'save')

    result = run_command(profile_switch, ['--profile', 'az'])
    spy_profile.assert_called_once_with('az')
    spy_save.assert_called_once_with()
    assert "✓ Switched to profile 'az'" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Switch profile (interactive mode)
    # ---------------------------------------------------------------

    spy_profile = mocker.spy(ConfigStore, 'change_active_profile')
    spy_save = mocker.spy(ConfigStore, 'save')

    fuzzy_mock = mocker.patch('relationalai.tools.cli_controls.fuzzy')
    fuzzy_mock.return_value = 'sf'

    result = run_command(profile_switch)

    spy_profile.assert_called_once_with('sf')
    spy_save.assert_called_once_with()
    assert "✓ Switched to profile 'sf'" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Clean slate - no profiles
    # ---------------------------------------------------------------

    # Kills all mocks - last in this test - position matters
    mocker.stopall()
    result = run_command(profile_switch)
    assert 'No profiles found' in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai engines:get
# ---------------------------------------------------------------
def test_engines_get(mocker):
    from relationalai.tools.cli import engines_get
    mocked_response = mocked_engines_list[1]
    text_mock = mocker.patch('relationalai.tools.cli_controls.text')
    instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value

    # ---------------------------------------------------------------
    #  Get the engine (non-interactive mode)
    # ---------------------------------------------------------------

    instance.get_engine.return_value = None

    result = run_command(engines_get, ['--name', 'baz'])
    assert 'Engine "baz" not found' in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Get the engine (interactive mode)
    # ---------------------------------------------------------------

    instance.get_engine.return_value = mocked_response

    # controls.text() is mocked to return "foo" here
    text_mock.return_value = "foo"

    result = run_command(engines_get)
    assert "foo    XS     READY" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Engine not found
    # ---------------------------------------------------------------

    instance.get_engine.return_value = None

    result = run_command(engines_get)
    assert 'Engine "foo" not found' in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Exception handling
    # ---------------------------------------------------------------

    with patch('relationalai.tools.cli.get_resource_provider', side_effect=Exception('Provider Error')):
        result = run_command(engines_get)

    assert "Error fetching engine: Provider Error" in result.output
    assert result.exit_code == 1

# ---------------------------------------------------------------
# rai engines:create - Snowflake
# ---------------------------------------------------------------
def test_engines_create_snowflake(mocker):
    import relationalai.tools.cli
    import relationalai.tools.cli_helpers
    import relationalai.clients.config

    mocker.stopall()
    mocker.patch('relationalai.tools.cli.validate_engine_name', return_value=True)

    provider_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value

    spy_validate_engine_name = mocker.spy(relationalai.tools.cli, 'validate_engine_name')
    spy_create_engine_flow = mocker.spy(relationalai.tools.cli, 'create_engine_flow')
    spy_create_engine = mocker.spy(provider_instance, 'create_engine')

    cfg = config.Config(sf_profile)
    mocker.patch('relationalai.tools.cli.ensure_config', return_value=cfg)

    result = run_command(relationalai.tools.cli.engines_create, ['--name', 'foo', '--size', 'HighMem|S', '--pool', 'BAZ'])

    spy_create_engine_flow.assert_called_once_with(cfg, 'foo', 'HighMem|S', 'BAZ')
    spy_validate_engine_name.assert_called_once_with(cfg, 'foo')
    spy_create_engine.assert_called_once_with('foo', 'HighMem|S', 'BAZ')
    assert "Engine 'foo' created!" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Engine already exists
    # ---------------------------------------------------------------

    mocker.stopall()

    provider_instance = mocker.patch('relationalai.tools.cli_helpers.get_resource_provider').return_value
    provider_instance.get_engine.return_value = {'name': 'foo', 'size': 'HighMem|S', 'state': 'READY'}

    mocker.patch('relationalai.tools.cli.ensure_config', return_value=cfg)

    result = run_command(relationalai.tools.cli.engines_create, ['--name', 'foo', '--size', 'HighMem|S', '--pool', 'BAZ'])
    assert "Engine 'foo' already exists" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Engine creation fails
    # ---------------------------------------------------------------

    mocker.stopall()

    provider_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    provider_instance.create_engine.side_effect = Exception('CREATE_ENGINE Error')

    mocker.patch('relationalai.tools.cli.validate_engine_name', return_value=True)
    mocker.patch('relationalai.tools.cli.ensure_config', return_value=cfg)

    result = run_command(relationalai.tools.cli.engines_create, ['--name', 'foo', '--size', 'HighMem|S', '--pool', 'BAZ'])

    assert "Error: CREATE_ENGINE Error" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai engines:create - Azure
# ---------------------------------------------------------------
def test_engines_create_azure(mocker):
    import relationalai.tools.cli
    import relationalai.clients.config

    mocker.stopall()
    mocker.patch('relationalai.tools.cli.validate_engine_name', return_value=True)

    provider_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value

    spy_validate_engine_name = mocker.spy(relationalai.tools.cli, 'validate_engine_name')
    spy_create_engine_flow = mocker.spy(relationalai.tools.cli, 'create_engine_flow')
    spy_create_engine = mocker.spy(provider_instance, 'create_engine')

    cfg = config.Config(az_profile)
    mocker.patch('relationalai.tools.cli.ensure_config', return_value=cfg)

    result = run_command(relationalai.tools.cli.engines_create, ['--name', 'baz', '--size', 'S'])

    spy_create_engine_flow.assert_called_with(cfg, 'baz', 'S', None)
    spy_validate_engine_name.assert_called_with(cfg, 'baz')
    spy_create_engine.assert_called_with('baz', 'S', '')
    assert "Engine 'baz' created!" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Engine already exists
    # ---------------------------------------------------------------

    mocker.stopall()

    provider_instance = mocker.patch('relationalai.tools.cli_helpers.get_resource_provider').return_value
    provider_instance.get_engine.return_value = {'name': 'baz', 'size': 'S', 'state': 'READY'}

    mocker.patch('relationalai.tools.cli.ensure_config', return_value=cfg)

    result = run_command(relationalai.tools.cli.engines_create, ['--name', 'baz', '--size', 'S'])
    assert "Engine 'baz' already exists" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Engine creation fails
    # ---------------------------------------------------------------

    mocker.stopall()
    mocker.patch('relationalai.tools.cli.validate_engine_name', return_value=True)

    provider_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    provider_instance.create_engine.side_effect = Exception('CREATE_ENGINE Error')

    mocker.patch('relationalai.tools.cli.ensure_config', return_value=cfg)

    result = run_command(relationalai.tools.cli.engines_create, ['--name', 'baz', '--size', 'S'])

    assert "Error: CREATE_ENGINE Error" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai engines:delete
# ---------------------------------------------------------------
def test_engines_delete(mocker):
    from relationalai.tools.cli import engines_delete
    instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value

    # ---------------------------------------------------------------
    #  Engine not found
    # ---------------------------------------------------------------

    instance.get_engine.return_value = None

    result = run_command(engines_delete, ['--name', 'baz'])
    assert "Engine 'baz' not found" in result.output
    assert result.exit_code == 1

    # ---------------------------------------------------------------
    #  Engine found - Delete engine
    # ---------------------------------------------------------------

    engine_response = {'name': 'foo', 'size': 'S', 'state': 'READY'}
    instance.get_engine.return_value = engine_response
    spy = mocker.spy(instance, 'delete_engine')

    result = run_command(engines_delete, ['--name', 'foo'])
    spy.assert_called_once_with('foo', False)
    assert "Engine 'foo' deleted!" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  SETUP_CDC Exception when no --force flag
    # ---------------------------------------------------------------

    instance.get_engine.return_value = [{'name': 'bar', 'size': 'S', 'state': 'READY'}]
    instance.delete_engine.side_effect = Exception('SETUP_CDC Error')

    result = run_command(engines_delete, ['--name', 'bar'])

    assert "Imports are setup to utilize this engine.\nUse 'rai engines:delete --force' to force delete engines.\nUse 'rai imports:setup --engine' to set a different engine for imports." in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  --force delete engine
    # ---------------------------------------------------------------

    instance.delete_engine.side_effect = None
    spy = mocker.spy(instance, 'delete_engine')

    result = run_command(engines_delete, ['--name', 'bar', '--force'])

    spy.assert_called_once_with('bar', True)
    assert "Engine 'bar' deleted!" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai engines:list
# ---------------------------------------------------------------
def test_engines_list(mocker):
    from relationalai.tools.cli import engines_list

    # ---------------------------------------------------------------
    #  Listing the engines
    # ---------------------------------------------------------------

    instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    instance.list_engines.return_value = mocked_engines_list

    result = run_command(engines_list)

    assert "1   test   XS     READY" in result.output
    assert "2   foo    XS     READY" in result.output
    assert "3   bar    S      READY" in result.output
    assert "4   baz    M      PENDING" in result.output
    assert "5   goo    M      SUSPENDED" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Listing the engines (Filter by state)
    # ---------------------------------------------------------------

    instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    spy = mocker.spy(instance, 'list_engines')

    result = run_command(engines_list, ['--state', 'ready'])

    spy.assert_called_once_with('ready')
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  No engines found
    # ---------------------------------------------------------------

    instance.list_engines.return_value = []

    result = run_command(engines_list)
    assert "No engines found" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Handle exception
    # ---------------------------------------------------------------

    with patch('relationalai.tools.cli.get_resource_provider', side_effect=Exception('Provider Error')):
        result = run_command(engines_list)

    assert "Error fetching engines: Provider Error" in result.output
    assert result.exit_code == 1

# ---------------------------------------------------------------
# rai version
# ---------------------------------------------------------------
def test_rai_version(mocker):
    from relationalai.tools.cli import version
    from relationalai import __version__ as rai_version
    from railib import __version__ as railib_version

    python_version = sys.version.split()[0]

    # ---------------------------------------------------------------
    #  No configuration file found with no latest version
    # ---------------------------------------------------------------

    instance = mocker.patch('relationalai.tools.cli.get_config').return_value
    instance.file_path = None

    latest_version = mocker.patch('relationalai.tools.cli.latest_version')
    latest_version.return_value = None

    result = run_command(version)

    assert f"RelationalAI   {rai_version}" in result.output
    assert f"Rai-sdk        {railib_version}" in result.output
    assert f"Python         {python_version}" in result.output
    assert "App            No configuration file found. To create one, run: rai init" in result.output
    assert "→" not in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  No configuration file found with latest version
    # ---------------------------------------------------------------

    latest_version.return_value = "10000.1.1"

    result = run_command(version)

    assert f"RelationalAI   {rai_version} → 10000.1.1" in result.output
    assert f"Rai-sdk        {railib_version} → 10000.1.1" in result.output
    assert f"Python         {python_version}" in result.output
    assert "App            No configuration file found. To create one, run: rai init" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Current is newer than latest
    # ---------------------------------------------------------------

    latest_version.return_value = "0.0.1"

    result = run_command(version)
    assert f"RelationalAI   {rai_version}" in result.output
    assert "→ 0.0.1" not in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Configuration file found - Snowflake - Show App version
    # ---------------------------------------------------------------

    instance = mocker.patch('relationalai.tools.cli.get_config').return_value
    instance.file_path = "some path"
    instance.get.return_value = "snowflake"

    instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    instance.get_version.return_value = "1.0.0"

    result = run_command(version)

    assert f"RelationalAI   {rai_version}" in result.output
    assert f"Rai-sdk        {railib_version}" in result.output
    assert f"Python         {python_version}" in result.output
    assert "App            1.0.0" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Configuration file found - Azure
    # ---------------------------------------------------------------

    instance = mocker.patch('relationalai.tools.cli.get_config').return_value
    instance.file_path = "some path"
    instance.get.return_value = "azure"

    result = run_command(version)

    assert f"RelationalAI   {rai_version}" in result.output
    assert f"Rai-sdk        {railib_version}" in result.output
    assert f"Python         {python_version}" in result.output
    assert "App" not in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Error getting versions - Azure/Snowflake
    # ---------------------------------------------------------------

    with patch('relationalai.tools.cli.get_config', side_effect=Exception('Config Error')):
        result = run_command(version)

    assert "Error checking app version: Config Error" in result.output
    assert result.exit_code == 1

    # ---------------------------------------------------------------
    #  Error getting app version - Snowflake specific
    # ---------------------------------------------------------------

    instance = mocker.patch('relationalai.tools.cli.get_config').return_value
    instance.file_path = "some path"
    instance.get.return_value = "snowflake"

    with patch('relationalai.tools.cli.get_resource_provider', side_effect=Exception('Provider Error')):
        result = run_command(version)

    assert f"RelationalAI   {rai_version}" in result.output
    assert f"Rai-sdk        {railib_version}" in result.output
    assert f"Python         {python_version}" in result.output
    assert "App   Provider Error" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai imports:get
# ---------------------------------------------------------------
def test_imports_get(mocker):
    from relationalai.tools.cli import imports_get

    mocker.stopall()

    mocker.patch.object(ConfigStore, 'get', return_value=None)
    mocker.patch('relationalai.clients.config._get_full_config', return_value=[sf_profile, "some path"])

    rp_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    rp_instance.list_imports.return_value = mocked_list_imports_response
    rp_instance.get_import_stream.return_value = mocked_import_stream_response

    # ---------------------------------------------------------------
    #  Interactive mode (no id provided)
    # ---------------------------------------------------------------
    mocker.patch('relationalai.tools.cli_controls.fuzzy', return_value='foo_id')

    result = run_command(imports_get)
    assert "Imports fetched" in result.output
    assert "1   foo_id   FOO    FOO     2024-06-03   JOE       1         LOADED" in result.output
    assert "2   bar_id   BAR    BAR     2024-01-01   JAKE      1         LOADED" in result.output
    assert "3   baz_id   BAZ    BAZ     2024-03-03   BLAKE     1         LOADED   err1" in result.output
    assert "Import details fetched" in result.output

    for detail in mocked_imports_get_details:
        assert detail in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Non-interactive mode (id provided)
    # ---------------------------------------------------------------
    result = run_command(imports_get, ['--id', 'foo_id'])

    assert "Imports fetched" in result.output
    assert "Import details fetched" in result.output

    for detail in mocked_imports_get_details:
        assert detail in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Non-interactive mode (provided id not found)
    # ---------------------------------------------------------------
    result = run_command(imports_get, ['--id', 'boo_id'])

    assert "Imports fetched" in result.output
    assert "Import 'boo_id' not found" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai imports:list
# ---------------------------------------------------------------
def test_imports_list(mocker):
    from relationalai.tools.cli import imports_list

    mocker.stopall()

    mocker.patch.object(ConfigStore, 'get', return_value=None)
    mocker.patch('relationalai.clients.config._get_full_config', return_value=[sf_profile, "some path"])

    rp_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    rp_instance.get_imports_status.return_value = mocked_imports_status
    rp_instance.list_imports.return_value = mocked_list_imports_response

    # ---------------------------------------------------------------
    #  Happy path with imports configured
    # ---------------------------------------------------------------
    result = run_command(imports_list)

    assert "Imports config fetched" in result.output
    assert "Imports status: STARTED" in result.output
    assert "Imports fetched" in result.output
    assert "1   FOO    FOO     2024-06-03   JOE       1         LOADED" in result.output
    assert "2   BAR    BAR     2024-01-01   JAKE      1         LOADED" in result.output
    assert "3   BAZ    BAZ     2024-03-03   BLAKE     1         LOADED   err1" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Filter by id
    # ---------------------------------------------------------------
    spy = mocker.spy(rp_instance, 'list_imports')
    result = run_command(imports_list, ['--id', 'baz_id'])
    spy.assert_called_once_with('baz_id', None, None, None, None)
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Filter by name
    # ---------------------------------------------------------------
    spy = mocker.spy(rp_instance, 'list_imports')
    result = run_command(imports_list, ['--name', 'FOO'])
    spy.assert_called_once_with(None, 'FOO', None, None, None)
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Filter by model
    # ---------------------------------------------------------------
    spy = mocker.spy(rp_instance, 'list_imports')
    result = run_command(imports_list, ['--model', 'MODEL'])
    spy.assert_called_once_with(None, None, 'MODEL', None, None)
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Filter by status
    # ---------------------------------------------------------------
    spy = mocker.spy(rp_instance, 'list_imports')
    result = run_command(imports_list, ['--status', 'ACTIVE'])
    spy.assert_called_once_with(None, None, None, 'ACTIVE', None)
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Filter by creator
    # ---------------------------------------------------------------
    spy = mocker.spy(rp_instance, 'list_imports')
    result = run_command(imports_list, ['--creator', 'JOE'])
    spy.assert_called_once_with(None, None, None, None, 'JOE')
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Filter by all
    # ---------------------------------------------------------------
    spy = mocker.spy(rp_instance, 'list_imports')
    result = run_command(imports_list, [
        '--id', 'baz_id',
        '--name', 'FOO',
        '--model', 'MODEL',
        '--status', 'ACTIVE',
        '--creator', 'JOE'
    ])
    spy.assert_called_once_with('baz_id', 'FOO', 'MODEL', 'ACTIVE', 'JOE')
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Imports not configured - "SETUP_CDC" in exception
    # ---------------------------------------------------------------
    rp_instance.get_imports_status.side_effect = Exception('SETUP_CDC')
    result = run_command(imports_list)

    assert "Error: Imports are not configured." in result.output
    assert "To start use 'rai imports:setup' to set up an engine for imports." in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  No imports found
    # ---------------------------------------------------------------
    get_rp = mocker.patch('relationalai.tools.cli.get_resource_provider')
    rp_instance = get_rp.return_value
    rp_instance.list_imports.return_value = []
    result = run_command(imports_list)

    assert "Imports fetched" in result.output
    assert "No imports found" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai imports:setup
# ---------------------------------------------------------------
def test_imports_setup(mocker):
    import relationalai.clients.config
    from relationalai.tools.cli import imports_setup

    mocker.stopall()

    mocker.patch.object(ConfigStore, 'get', return_value=None)
    mocker.patch('relationalai.clients.config._get_full_config', return_value=[sf_profile, "some path"])

    rp_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    rp_instance.get_imports_status.return_value = mocked_imports_status

    # ---------------------------------------------------------------
    #  Display imports setup
    # ---------------------------------------------------------------

    result = run_command(imports_setup)

    assert "To suspend imports, use 'rai imports:setup --suspend'" in result.output
    assert "Field                 Value" in result.output
    assert "engine                FOO_ENG" in result.output
    assert "status                STARTED" in result.output
    assert "createdOn             2024-06-03 10:50:04" in result.output
    assert "lastSuspendedOn       N/A" in result.output
    assert "lastSuspendedReason   N/A" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Imports suspended
    # ---------------------------------------------------------------

    mocked_imports_status["status"] = 'suspended'
    mocked_imports_status["info"] = '{\n  "createdOn": "2024-06-03 10:50:04.735 -0700",\n  "lastSuspendedOn": "2024-06-13 10:50:04.735 -0700",\n  "lastSuspendedReason": "USER_SUSPENDED",\n  "state": "suspended"\n}'
    rp_instance.get_imports_status.return_value = mocked_imports_status
    result = run_command(imports_setup)

    assert "To resume imports, use 'rai imports:setup --resume'" in result.output
    assert "status                SUSPENDED" in result.output
    assert "createdOn             2024-06-03 10:50:04" in result.output
    assert "lastSuspendedOn       2024-06-13 10:50:04" in result.output
    assert "lastSuspendedReason   USER_SUSPENDED" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Suspend imports
    # ---------------------------------------------------------------

    spy_change_status = mocker.spy(rp_instance, 'change_imports_status')
    result = run_command(imports_setup, ['--suspend'])

    spy_change_status.assert_called_once_with(suspend=True)
    assert "Imports suspended" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Resume imports
    # ---------------------------------------------------------------

    spy_change_status = mocker.spy(rp_instance, 'change_imports_status')
    result = run_command(imports_setup, ['--resume'])

    spy_change_status.assert_called_once_with(suspend=False)
    assert "Imports resumed" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Setup with passed in engine
    # ---------------------------------------------------------------

    spy_set_engine = mocker.spy(relationalai.tools.cli, 'set_imports_engine')
    rp_instance.get_engine.return_value = mocked_engines_list[1]

    result = run_command(imports_setup, ['--engine', 'foo'])

    spy_set_engine.assert_called_once_with('foo')
    assert "Engine validated" in result.output
    assert "Imports engine set to 'foo'" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Setup with invalid engine
    # ---------------------------------------------------------------

    rp_instance.get_engine.return_value = None
    result = run_command(imports_setup, ['--engine', 'foo'])

    assert "Engine 'foo' is invalid." in result.output
    assert "Please use 'rai engines:create' to create a valid engine." in result.output

    # ---------------------------------------------------------------
    #  Exception handling
    # ---------------------------------------------------------------

    rp_instance.get_engine.side_effect = Exception('GET_IMPORTS_STATUS Error')

    result = run_command(imports_setup, ['--engine', 'foo'])

    assert "Error: GET_IMPORTS_STATUS Error" in result.output
    assert result.exit_code == 1

# ---------------------------------------------------------------
# rai transactions:list (snowflake)
# ---------------------------------------------------------------
def test_transactions_list_snowflake(mocker):
    from relationalai.clients.snowflake import Resources
    from relationalai.tools.cli import transactions_list

    mocker.stopall()

    cfg = config.Config(sf_profile)
    mocker.patch('relationalai.tools.cli.ensure_config', return_value=cfg)
    mocker.patch('relationalai.tools.cli_helpers.ensure_config', return_value=cfg)

    snowflake = Resources(config=cfg)
    mocker.patch('relationalai.tools.cli.get_resource_provider', return_value=snowflake)

    _exec = mocker.patch('relationalai.clients.snowflake.Resources._exec')
    txn_list_to_dicts = mocker.patch('relationalai.clients.snowflake.Resources.txn_list_to_dicts')

    SELECT = "select id, database_name, engine_name, state, abort_reason, read_only, created_by, created_on, finished_at, duration from ___RAI_APP___.api.transactions"

    # ---------------------------------------------------------------
    #  Snowflake - No transactions found
    # ---------------------------------------------------------------

    result = run_command(transactions_list)
    _exec.assert_called_once_with(f"{SELECT}  LIMIT ?", [100])
    assert "No transactions found" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Snowflake - Transactions list all users
    # ---------------------------------------------------------------

    _exec = mocker.patch('relationalai.clients.snowflake.Resources._exec')
    txn_list_to_dicts.return_value = mocked_txns_list_snowflake

    result = run_command(transactions_list, ['--all-users'])
    _exec.assert_called_once_with(f"{SELECT}  LIMIT ?", [100])
    assert "1   id1   db1      FOO      COMPLETED   2024-06-17 07:11:17       1.6s" in result.output
    assert "2   id2   db2      BAR      ABORTED     2024-06-17 07:11:15       0.6s" in result.output
    assert "3   id3   db3      BAZ      COMPLETED   2024-06-17 07:11:03       8.5s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Snowflake - Transactions list filter by id
    # ---------------------------------------------------------------

    _exec = mocker.patch('relationalai.clients.snowflake.Resources._exec')
    txn_list_to_dicts.return_value = [mocked_txns_list_snowflake[1]]

    result = run_command(transactions_list, ['--id', 'id2'])
    _exec.assert_called_once_with(f"{SELECT} WHERE id = 'id2' LIMIT ?", [100])
    assert "id1" not in result.output
    assert "id3" not in result.output
    assert "1   id2   db2      BAR      ABORTED   2024-06-17 07:11:15       0.6s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Snowflake - Transactions list filter by engine
    # ---------------------------------------------------------------

    _exec = mocker.patch('relationalai.clients.snowflake.Resources._exec')

    result = run_command(transactions_list, ['--engine', 'BAR'])
    _exec.assert_called_once_with(f"{SELECT} WHERE LOWER(engine_name) = 'bar' LIMIT ?", [100])
    assert "id1" not in result.output
    assert "id3" not in result.output
    assert "1   id2   db2      BAR      ABORTED   2024-06-17 07:11:15       0.6s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Snowflake - Transactions list filter by state
    # ---------------------------------------------------------------

    _exec = mocker.patch('relationalai.clients.snowflake.Resources._exec')

    result = run_command(transactions_list, ['--state', 'ABORTED'])
    _exec.assert_called_once_with(f"{SELECT} WHERE state = 'ABORTED' LIMIT ?", [100])
    assert "id1" not in result.output
    assert "id3" not in result.output
    assert "1   id2   db2      BAR      ABORTED   2024-06-17 07:11:15       0.6s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Snowflake - Transactions list filter by state (all users)
    # ---------------------------------------------------------------

    _exec = mocker.patch('relationalai.clients.snowflake.Resources._exec')
    txn_list_to_dicts.return_value = [mocked_txns_list_snowflake[0], mocked_txns_list_snowflake[2]]

    result = run_command(transactions_list, ['--all-users', '--state', 'COMPLETED'])
    _exec.assert_called_once_with(f"{SELECT} WHERE state = 'COMPLETED' LIMIT ?", [100])
    assert "id2" not in result.output
    assert "1   id1   db1      FOO      COMPLETED   2024-06-17 07:11:17       1.6s" in result.output
    assert "2   id3   db3      BAZ      COMPLETED   2024-06-17 07:11:03       8.5s" in result.output
    assert result.exit_code == 0

    # --------------------------------------------------------------------------
    #  Snowflake - Transactions list (all users) and limit to 2
    # --------------------------------------------------------------------------

    _exec = mocker.patch('relationalai.clients.snowflake.Resources._exec')
    txn_list_to_dicts.return_value = [mocked_txns_list_snowflake[0], mocked_txns_list_snowflake[1]]

    result = run_command(transactions_list, ['--limit', 2])
    _exec.assert_called_once_with(f"{SELECT}  LIMIT ?", [100])
    assert "id3" not in result.output
    assert "1   id1   db1      FOO      COMPLETED   2024-06-17 07:11:17       1.6s" in result.output
    assert "2   id2   db2      BAR      ABORTED     2024-06-17 07:11:15       0.6s" in result.output
    assert result.exit_code == 0

# ---------------------------------------------------------------
# rai transactions:list (azure)
# ---------------------------------------------------------------
def test_transactions_list_azure(mocker):
    from relationalai.tools.cli import transactions_list

    mocker.stopall()

    cfg = config.Config(az_profile)
    rp_instance = mocker.patch('relationalai.tools.cli.get_resource_provider').return_value
    rp_instance.config.return_value = cfg

    rp_instance_helpers = mocker.patch('relationalai.tools.cli_helpers.get_resource_provider').return_value
    rp_instance_helpers.config.return_value = cfg

    # ---------------------------------------------------------------
    #  Azure - No transactions found
    # ---------------------------------------------------------------

    rp_instance.list_transactions.return_value = []
    result = run_command(transactions_list)
    assert "No transactions found" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Azure - Transactions list all users
    # ---------------------------------------------------------------

    rp_instance.list_transactions.return_value = mocked_txns_list_azure
    result = run_command(transactions_list)
    assert "1   id1   db1      FOO      COMPLETED   2024-06-14 18:22:02       0.4s" in result.output
    assert "2   id2   db2      BAR      ABORTED     2024-06-14 18:22:02       0.2s" in result.output
    assert "3   id3   db3      BAZ      COMPLETED   2024-06-14 18:08:35       0.9s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Azure - Transactions list filter by id
    # ---------------------------------------------------------------

    rp_instance.list_transactions.return_value = [mocked_txns_list_azure[1]]
    result = run_command(transactions_list, ['--id', 'id2'])
    assert "id1" not in result.output
    assert "id3" not in result.output
    assert "1   id2   db2      BAR      ABORTED   2024-06-14 18:22:02       0.2s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Azure - Transactions list filter by engine
    # ---------------------------------------------------------------
    result = run_command(transactions_list, ['--engine', 'BAR'])
    assert "id1" not in result.output
    assert "id3" not in result.output
    assert "1   id2   db2      BAR      ABORTED   2024-06-14 18:22:02       0.2s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Azure - Transactions list filter by state
    # ---------------------------------------------------------------

    result = run_command(transactions_list, ['--state', 'ABORTED'])
    assert "id1" not in result.output
    assert "id3" not in result.output
    assert "1   id2   db2      BAR      ABORTED   2024-06-14 18:22:02       0.2s" in result.output
    assert result.exit_code == 0

    # ---------------------------------------------------------------
    #  Azure - Transactions list filter by state
    # ---------------------------------------------------------------

    rp_instance.list_transactions.return_value = [mocked_txns_list_azure[0], mocked_txns_list_azure[2]]
    result = run_command(transactions_list, ['--state', 'COMPLETED'])
    assert "id2" not in result.output
    assert "1   id1   db1      FOO      COMPLETED   2024-06-14 18:22:02       0.4s" in result.output
    assert "2   id3   db3      BAZ      COMPLETED   2024-06-14 18:08:35       0.9s" in result.output
    assert result.exit_code == 0

    # --------------------------------------------------------------------------
    #  Azure - Transactions list and limit to 2
    # --------------------------------------------------------------------------

    rp_instance.list_transactions.return_value = [mocked_txns_list_azure[0], mocked_txns_list_azure[1]]
    result = run_command(transactions_list, ['--limit', 2])
    assert "id3" not in result.output
    assert "1   id1   db1      FOO      COMPLETED   2024-06-14 18:22:02       0.4s" in result.output
    assert "2   id2   db2      BAR      ABORTED     2024-06-14 18:22:02       0.2s" in result.output
    assert result.exit_code == 0
