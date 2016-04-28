from copy import deepcopy

from config import GLOBAL_VARS, PLATFORM_VARS, SLAVES, TRY_SLAVES

import b2g_project_branches
reload(b2g_project_branches)
from b2g_project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

# Note that b2g_localconfig.py is symlinked to one of:
# {production,staging}_b2g_config.py
import b2g_localconfig
reload(b2g_localconfig)

import master_common
reload(master_common)
from master_common import items_before, setMainFirefoxVersions, items_at_least

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
PLATFORM_VARS = deepcopy(PLATFORM_VARS)

GLOBAL_VARS.update(b2g_localconfig.GLOBAL_VARS.copy())

GLOBAL_VARS.update({
    'platforms': {
        'nexus-4': {},
        'nexus-4_eng': {},
        'nexus-5-l': {},
        'nexus-5-l_eng': {},
        'emulator': {},
        'emulator-debug': {},
        'flame-kk': {},
        'flame-kk_eng': {},
        'flame-kk_eng-debug': {},
    },
    'enable_nightly': True,
    'enable_l10n': False,
    'enabled_products': ['b2g', 'graphene', 'horizon'],
    'product_prefix': 'b2g',
    'unittest_suites': [],
    # XXX: this seems like it should be at the platform level
    'enable_multi_locale': True,
})

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
builder_prefix = "b2g"
gaia_repo = 'integration/gaia-central'
gaia_revision_file = 'b2g/config/gaia.json'

GLOBAL_ENV = {
    'MOZ_CRASHREPORTER_NO_REPORT': '1',
    'TINDERBOX_OUTPUT': '1',
    'MOZ_AUTOMATION': '1',
}

PLATFORM_VARS = {
    'nexus-4': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-4', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'nexus-4_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-4', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'nexus-5-l': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-5-l', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'nexus-5-l_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'nexus-5-l', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'PATH': '/tools/python27-mercurial/bin:/tools/python27/bin:/usr/local/bin:/usr/lib64/ccache:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/cltbld/bin',
            'PYTHONPATH': '/tools/python27/lib',
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'emulator': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'try_by_default': False,
        'maxTime': 6 * 3600,
    },
    'emulator-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'try_by_default': False,
        'maxTime': 6 * 3600,
    },
    'emulator-jb': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-jb', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
        'maxTime': 6 * 3600,
    },
    'emulator-jb-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-jb', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'emulator-kk': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-kk', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'emulator-kk-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-kk', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'emulator-l': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-l', '--config', 'b2g/releng-emulator.py',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
        'maxTime': 6 * 3600,
    },
    'emulator-l-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'emulator-l', '--config', 'b2g/releng-emulator.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_dev.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
        'maxTime': 6 * 3600,
    },
    'flame-kk': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame-kk', '--config', 'b2g/releng-fota-updates.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'flame-kk_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame-kk', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': False,
        'enable_dep': True,
    },
    'flame-kk_eng-debug': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'flame-kk', '--config', 'b2g/releng-otoro-eng.py',
                           '--debug',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'dolphin': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'dolphin_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'dolphin-512': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin-512', '--config', 'b2g/releng-private-updates.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales',
                           '--config', GLOBAL_VARS['mozharness_configs']['balrog']],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    'dolphin-512_eng': {
        'mozharness_config': {
            'script_name': 'scripts/b2g_build.py',
            # b2g_build.py will checkout gecko from hg and look up a tooltool manifest given by the
            # --target name below
            'extra_args': ['--target', 'dolphin-512', '--config', 'b2g/releng-otoro-eng.py',
                           '--gaia-languages-file', 'locales/languages_all.json',
                           '--gecko-languages-file', 'gecko/b2g/locales/all-locales'],
            'reboot_command': ['bash', '-c', 'sudo reboot; sleep 600'],
            'mozharness_repo_cache': '/tools/checkouts/mozharness',
            'tools_repo_cache': '/tools/checkouts/build-tools',
        },
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
        },
        'stage_product': 'b2g',
        'product_name': 'b2g',
        'base_name': builder_prefix + '_%(branch)s_%(platform)s',
        'slaves': SLAVES['mock'],
        'enable_periodic': True,
        'enable_dep': False,
    },
    "linux64_graphene": {
        "mozharness_python": "/tools/buildbot/bin/python",
        "reboot_command": [
            "/tools/checkouts/mozharness/external_tools/count_and_reboot.py",
            "-f", "../reboot_count.txt", "-n", "1", "-z"
        ],
        "mozharness_repo_cache": "/tools/checkouts/mozharness",
        "tools_repo_cache": "/tools/checkouts/build-tools",
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_linux_64_builds.py",
                "--custom-build-variant-cfg", "graphene",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "graphene_%(branch)s_linux64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["mock"],
        "try_by_default": False,
    },
    "macosx64_graphene": {
        "mozharness_python": "/tools/buildbot/bin/python",
        "reboot_command": ["scripts/external_tools/count_and_reboot.py",
                           "-f", "../reboot_count.txt", "-n", "1", "-z"],
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_mac_64_builds.py",
                "--custom-build-variant-cfg", "graphene",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "graphene_%(branch)s_macosx64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["macosx64-lion"],
        "try_by_default": False,
    },
    "win64_graphene": {
        "mozharness_python": ["c:/mozilla-build/python27/python", "-u"],
        "reboot_command": [
            "c:/mozilla-build/python27/python", "-u",
            "scripts/external_tools/count_and_reboot.py",
            "-f", "../reboot_count.txt","-n", "1", "-z"
        ],
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_windows_64_builds.py",
                "--custom-build-variant-cfg", "graphene",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "graphene_%(branch)s_win64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["win64-rev2"],
        "try_by_default": False,
    },
    "linux64_horizon": {
        "mozharness_python": "/tools/buildbot/bin/python",
        "reboot_command": [
            "/tools/checkouts/mozharness/external_tools/count_and_reboot.py",
            "-f", "../reboot_count.txt", "-n", "1", "-z"
        ],
        "mozharness_repo_cache": "/tools/checkouts/mozharness",
        "tools_repo_cache": "/tools/checkouts/build-tools",
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_linux_64_builds.py",
                "--custom-build-variant-cfg", "horizon",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "horizon_%(branch)s_linux64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["mock"],
        "try_by_default": False,
    },
    "macosx64_horizon": {
        "mozharness_python": "/tools/buildbot/bin/python",
        "reboot_command": ["scripts/external_tools/count_and_reboot.py",
                           "-f", "../reboot_count.txt", "-n", "1", "-z"],
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_mac_64_builds.py",
                "--custom-build-variant-cfg", "horizon",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "horizon_%(branch)s_macosx64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["macosx64-lion"],
        "try_by_default": False,
    },
    "win64_horizon": {
        "mozharness_python": ["c:/mozilla-build/python27/python", "-u"],
        "reboot_command": [
            "c:/mozilla-build/python27/python", "-u",
            "scripts/external_tools/count_and_reboot.py",
            "-f", "../reboot_count.txt","-n", "1", "-z"
        ],
        "mozharness_desktop_build": {
            "script_name": "scripts/fx_desktop_build.py",
            "extra_args": [
                "--config", "builds/releng_base_windows_64_builds.py",
                "--custom-build-variant-cfg", "horizon",
                '--config', GLOBAL_VARS['mozharness_configs']['balrog'],
            ],
            "script_timeout": 3 * 3600,
            "script_maxtime": int(5.5 * 3600),
        },
        "stage_product": "b2g",
        "base_name": "horizon_%(branch)s_win64",
        "platform_objdir": OBJDIR,
        "slaves": SLAVES["win64-rev2"],
        "try_by_default": False,
    },
}

for platform in PLATFORM_VARS.values():
    if 'env' not in platform:
        platform['env'] = deepcopy(GLOBAL_ENV)
    else:
        platform['env'].update((k, v) for k, v in GLOBAL_ENV.items() if k not in platform['env'])


# All branches (not in project_branches) that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
    },
    'mozilla-b2g44_v2_5': {
        'gecko_version': 44,
        'b2g_version': (2, 5, 0),
        'lock_platforms': True,
        'platforms': {
            'emulator': {},
            'emulator-debug': {},
            'emulator-l': {},
            'emulator-l-debug': {},
            'flame-kk': {},
            'flame-kk_eng': {},
        },
    },
    'try': {
        'lock_platforms': True,
        'platforms': {
            'linux64_graphene': {},
            'macosx64_graphene': {},
            'win64_graphene': {},
            'linux64_horizon': {},
            'macosx64_horizon': {},
            'win64_horizon': {},
            'emulator': {},
            'emulator-debug': {},
            # Graphene builds. These are a different app (ie, not B2G) and would
            # have their own config files in an ideal world, but it's not worth
            # the effort at this point.
            'linux64_graphene': {},
            'macosx64_graphene': {},
            'win64_graphene': {},
            # Horizon is a browser variant based on Graphene.
            'linux64_horizon': {},
            'macosx64_horizon': {},
            'win64_horizon': {},
        },
    },
}

setMainFirefoxVersions(BRANCHES)

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        else:
            BRANCHES[branch][key] = deepcopy(value)

        # bug 1218589 - Enable nightly mozilla-central builds of graphene     
        if key == 'platforms' and branch == 'mozilla-central':
            graphene = {'linux64_graphene': {}, 'macosx64_graphene': {}, 'win64_graphene': {}}
            BRANCHES[branch][key].update(graphene)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                # put default platform set in all branches, but grab any
                # project_branches.py overrides/additional keys
                if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch]:
                    if platform in PROJECT_BRANCHES[branch]['platforms'].keys():
                        if key in PROJECT_BRANCHES[branch]['platforms'][platform].keys():
                            value = deepcopy(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                else:
                    value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                else:
                    value = deepcopy(value)
                BRANCHES[branch]['platforms'][platform][key] = value

            if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch] and \
                    platform in PROJECT_BRANCHES[branch]['platforms']:
                for key, value in PROJECT_BRANCHES[branch]['platforms'][platform].items():
                    if key == 'env':
                        value = deepcopy(PLATFORM_VARS[platform]['env'])
                        value.update(PROJECT_BRANCHES[branch]['platforms'][platform][key])
                    else:
                        value = deepcopy(value)
                    BRANCHES[branch]['platforms'][platform][key] = value
    # Copy in local config
    if branch in b2g_localconfig.BRANCHES:
        for key, value in b2g_localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in b2g_localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Check for project branch removing a platform from default platforms
    if branch in ACTIVE_PROJECT_BRANCHES:
        for key, value in PROJECT_BRANCHES[branch].items():
            if key == 'platforms':
                for platform, platform_config in value.items():
                    if platform_config.get('dont_build'):
                        del BRANCHES[branch]['platforms'][platform]


######## remove most B2G builds from cedar
for platform in ('nexus-4', 'nexus-4_eng', 'nexus-5-l', 'nexus-5-l_eng',
                 'flame-kk', 'flame-kk_eng', 'flame-kk_eng-debug'):
    if platform in BRANCHES['cedar']['platforms']:
        del BRANCHES['cedar']['platforms'][platform]

# bug 1222209 - Remove nexus-4 builds from pine
for platform in ('nexus-4', 'nexus-4_eng'):
    if platform in BRANCHES['pine']['platforms']:
        del BRANCHES['pine']['platforms'][platform]

######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
BRANCHES['mozilla-central']['gecko_l10n_root'] = 'https://hg.mozilla.org/l10n-central'
BRANCHES['mozilla-central']['start_hour'] = [3, 15]
BRANCHES['mozilla-central']['start_minute'] = [2]
BRANCHES['mozilla-central']['periodic_start_hours'] = range(1, 24, 3)
BRANCHES['mozilla-central']['periodic_start_minute'] = 30
BRANCHES['mozilla-central']['platforms']['nexus-4']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-4_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-4_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-central']['platforms']['nexus-5-l']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-5-l_eng']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['nexus-5-l_eng']['consider_for_nightly'] = False
BRANCHES['mozilla-central']['platforms']['flame-kk']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['flame-kk_eng']['enable_nightly'] = True
# bug 1218589 - Enable nightly mozilla-central builds of graphene     
BRANCHES['mozilla-central']['platforms']['linux64_graphene']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['macosx64_graphene']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['win64_graphene']['enable_nightly'] = True
BRANCHES['mozilla-central']['platforms']['linux64_graphene']['slaves'] = SLAVES['mock']
BRANCHES['mozilla-central']['platforms']['macosx64_graphene']['slaves'] = SLAVES['macosx64-lion']
BRANCHES['mozilla-central']['platforms']['win64_graphene']['slaves'] = SLAVES['win64-rev2']


######## mozilla-b2g44_v2_5
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-b2g44_v2_5']['repo_path'] = 'releases/mozilla-b2g44_v2_5'
# TODO: coordinate l1n repos with bug 1218060
BRANCHES['mozilla-b2g44_v2_5']['gaia_l10n_root'] = 'https://hg.mozilla.org/releases/gaia-l10n/v2_5'
BRANCHES['mozilla-b2g44_v2_5']['gecko_l10n_root'] = 'https://hg.mozilla.org/releases/l10n/mozilla-aurora'
BRANCHES['mozilla-b2g44_v2_5']['start_hour'] = [0]
BRANCHES['mozilla-b2g44_v2_5']['start_minute'] = [45]
BRANCHES['mozilla-b2g44_v2_5']['periodic_start_minute'] = 30
BRANCHES['mozilla-b2g44_v2_5']['platforms']['flame-kk']['enable_nightly'] = True
BRANCHES['mozilla-b2g44_v2_5']['platforms']['flame-kk_eng']['enable_nightly'] = True
BRANCHES['mozilla-b2g44_v2_5']['platforms']['emulator']['enable_nightly'] = False
BRANCHES['mozilla-b2g44_v2_5']['platforms']['emulator-debug']['enable_nightly'] = False
BRANCHES['mozilla-b2g44_v2_5']['platforms']['emulator-l']['enable_nightly'] = False
BRANCHES['mozilla-b2g44_v2_5']['platforms']['emulator-l-debug']['enable_nightly'] = False

######## try
# Try-specific configs
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['try']['repo_path'] = 'try'
BRANCHES['try']['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
BRANCHES['try']['gecko_l10n_root'] = 'https://hg.mozilla.org/l10n-central'
BRANCHES['try']['enable_merging'] = False
BRANCHES['try']['enable_try'] = True
BRANCHES['try']['package_dir'] = '%(who)s-%(got_revision)s/'
BRANCHES['try']['stage_username'] = 'trybld'
BRANCHES['try']['stage_ssh_key'] = 'trybld_dsa'
# Disable Nightly builds
BRANCHES['try']['enable_nightly'] = False
BRANCHES['try']['platforms']['linux64_graphene']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['macosx64_graphene']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['win64_graphene']['slaves'] = TRY_SLAVES['win64-rev2']
BRANCHES['try']['platforms']['linux64_horizon']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['macosx64_horizon']['slaves'] = TRY_SLAVES['macosx64-lion']
BRANCHES['try']['platforms']['win64_horizon']['slaves'] = TRY_SLAVES['win64-rev2']

BRANCHES['try']['platforms']['emulator']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator']['mozharness_config']['extra_args'] = ['--target', 'emulator', '--config', 'b2g/releng-try.py', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']
BRANCHES['try']['platforms']['emulator-debug']['slaves'] = TRY_SLAVES['mock']
BRANCHES['try']['platforms']['emulator-debug']['mozharness_config']['extra_args'] = ['--target', 'emulator', '--config', 'b2g/releng-try.py', '--debug', '--gaia-languages-file', 'locales/languages_dev.json', '--gecko-languages-file', 'gecko/b2g/locales/all-locales']

# Enable mozharness pinning
for name, branch in items_at_least(BRANCHES, 'gecko_version', 30):
    branch['script_repo_manifest'] = \
        "https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/" + \
        "testing/mozharness/mozharness.json"
    # mozharness_archiver_repo_path tells the factory to use a copy of mozharness from within the
    #  gecko tree and also allows us to overwrite which gecko repo to use. Useful for platforms
    # like Thunderbird
    branch['mozharness_archiver_repo_path'] = '%(repo_path)s'

# Enable mozharness desktop builds
for name, branch in items_at_least(BRANCHES, 'gecko_version', 39):
    # if true, any platform with mozharness_desktop_build in its config
    # will use mozharness instead of MozillaBuildFactory
    branch['desktop_mozharness_builds_enabled'] = True

# v1.12.20 causes bug 1165727, using v1.12.16 instead
for branch in BRANCHES:
    for platform in BRANCHES[branch]['platforms']:
        if BRANCHES[branch]['platforms'][platform].get('mozharness_config', {}).get('extra_args'):
            BRANCHES[branch]['platforms'][platform]['mozharness_config']['extra_args'].extend(
                ['--repotool-revision', 'v1.12.16'])

######## generic branch configs
for branch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[branch]
    BRANCHES[branch]['gaia_l10n_root'] = 'https://hg.mozilla.org/gaia-l10n'
    BRANCHES[branch]['gecko_l10n_root'] = 'https://hg.mozilla.org/l10n-central'
    BRANCHES[branch]['product_name'] = branchConfig.get('product_name', None)
    BRANCHES[branch]['app_name'] = branchConfig.get('app_name', None)
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch)
    BRANCHES[branch]['mozharness_repo_path'] = branchConfig.get('mozharness_repo_path', GLOBAL_VARS['mozharness_repo_path'])
    BRANCHES[branch]['mozharness_tag'] = branchConfig.get('mozharness_tag', GLOBAL_VARS['mozharness_tag'])
    BRANCHES[branch]['enabled_products'] = branchConfig.get('enabled_products',
                                                            GLOBAL_VARS['enabled_products'])
    BRANCHES[branch]['enable_nightly'] = branchConfig.get('enable_nightly', False)
    BRANCHES[branch]['enable_nightly_everytime'] = branchConfig.get('enable_nightly_everytime', False)
    BRANCHES[branch]['periodic_start_hours'] = branchConfig.get('periodic_start_hours', range(0, 24, 6))
    BRANCHES[branch]['periodic_start_minute'] = branchConfig.get('periodic_start_minute', 30)
    BRANCHES[branch]['start_hour'] = branchConfig.get('start_hour', [4])
    BRANCHES[branch]['start_minute'] = branchConfig.get('start_minute', [42])
    # nightly updates
    BRANCHES[branch]['updates_enabled'] = branchConfig.get('updates_enabled', False)
    BRANCHES[branch]['update_channel'] = branchConfig.get('update_channel', 'nightly-%s' % branch)
    BRANCHES[branch]['create_partial'] = branchConfig.get('create_partial', False)
    BRANCHES[branch]['create_partial_l10n'] = branchConfig.get('create_partial_l10n', False)
    BRANCHES[branch]['enUS_binaryURL'] = GLOBAL_VARS['download_base_url'] + branchConfig.get('enUS_binaryURL', '')
    # Platform-specific defaults/interpretation
    for platform in BRANCHES[branch]['platforms']:
        # point to the mozconfigs, default is generic
        if platform.endswith('debug'):
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/debug'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/' + branchConfig.get('mozconfig_dir', 'generic') + '/nightly'

# bug 1227277 - Disabling b2g builds on project branches other than pine
B2GTWIGS = [x for x in ACTIVE_PROJECT_BRANCHES if x not in ('mozilla-inbound', 'fx-team', 'pine')]
for branch in B2GTWIGS:
    for platform in GLOBAL_VARS['platforms']:
        if branch not in BRANCHES:
            continue
        if platform in BRANCHES[branch]['platforms']:
            del BRANCHES[branch]['platforms'][platform]

# Bug 1250953 - Disable ICS emulator builds/tests on trunk
for branch in BRANCHES.keys():
    for platform in BRANCHES[branch]['platforms'].keys():
        if branch in ['mozilla-b2g44_v2_5', 'try']:
            continue
        if platform in ['emulator', 'emulator-debug']:
            del BRANCHES[branch]['platforms'][platform]

# Bug 1253630 - Turn off B2G device builds on trunk branches (buildbot only)
for name, branch in items_at_least(BRANCHES, 'gecko_version', 47):
    for platform in BRANCHES[name]['platforms'].keys():
        if platform in ['flame-kk', 'flame-kk_eng', 'nexus-4', 'nexus-4_eng', 'nexus-5-l', 'nexus-5-l_eng']:
            del BRANCHES[name]['platforms'][platform]

if __name__ == "__main__":
    import sys
    import pprint

    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = BRANCHES

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)
