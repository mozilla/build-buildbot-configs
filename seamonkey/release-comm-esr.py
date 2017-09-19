releaseConfig = {}

# Release Notification
#  not used yet
# Basic product configuration
#  Names for the product/files
releaseConfig['productName']                = 'seamonkey'
releaseConfig['brandName']                  = 'SeaMonkey'
releaseConfig['appName']                    = 'suite'
releaseConfig['binaryName']                 = releaseConfig['brandName']
releaseConfig['oldBinaryName']              = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']                    = '2.49.1'
releaseConfig['appVersion']                 = '2.49.1'
releaseConfig['milestone']                  = '52.4'
releaseConfig['buildNumber']                = 1
releaseConfig['baseTag']                    = 'SEAMONKEY_2_49_1'
#  Old version info
releaseConfig['oldVersion']                 = '2.48'
releaseConfig['oldAppVersion']              = '2.48'
releaseConfig['oldBuildNumber']             = 1
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_48'
releaseConfig['oldRepoPath']                = 'releases/comm-release'
#  Next (nightly) version info
#     not yet available
#  Repository configuration, for tagging
releaseConfig['skip_tag']                   = False
releaseConfig['relbranchPrefix']            = 'SEA_COMM'
releaseConfig['sourceRepoName']             = 'comm-esr' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-esr52'
releaseConfig['sourceRepoRevision']         = '7b09aa9b64bd'
releaseConfig['relbranchOverride']          = 'SEAMONKEY_2_49_ESR_RELBRANCH'
releaseConfig['productVersionFile']         = 'suite/config/version.txt'
#releaseConfig['productVersionFile']         = ''
#   Mozilla
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-esr52'
releaseConfig['mozillaRepoRevision']        = 'c3c8a7968114'
releaseConfig['mozillaRelbranchOverride']   = 'THUNDERBIRD_52_VERBRANCH' # put Gecko relbranch here that we base upon
#   Inspector
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = 'DOMI_2_0_17'
releaseConfig['inspectorRelbranchOverride'] = ''
#   Venkman
releaseConfig['venkmanRepoPath']            = '' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = ''
releaseConfig['venkmanRelbranchOverride']   = ''
#   Chatzilla
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = 'SEA2_48_RELBRANCH'
releaseConfig['chatzillaRelbranchOverride'] = ''
#  L10n repositories
releaseConfig['l10nRepoPath']               = 'releases/l10n/mozilla-release'
releaseConfig['l10nRelbranchOverride']      = ''
releaseConfig['l10nRevisionFile']           = 'l10n-changesets-comm-esr'
#  Support repositories
#   not used yet

# Platform configuration
releaseConfig['enUSPlatforms']              = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['talosTestPlatforms']         = ()

# Unittests
releaseConfig['unittestPlatforms']          = ()

# L10n configuration
releaseConfig['l10nPlatforms']              = ('linux', 'win32', 'macosx64')
releaseConfig['mergeLocales']               = True

# Mercurial account
releaseConfig['hgUsername']                 = 'seabld'
releaseConfig['hgSshKey']                   = '~seabld/.ssh/seabld_dsa'

# Update-specific configuration
releaseConfig['patcherConfig']              = 'mozEsr-seamonkey-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']            = 'UPDATE_PACKAGING_R18'
releaseConfig['ftpServer']                  = 'archive.mozilla.org'
releaseConfig['stagingServer']              = 'archive.mozilla.org'
releaseConfig['stagingUploadServer']        = 'upload.seabld.productdelivery.prod.mozaws.net'
releaseConfig['S3Credentials']              = '/builds/release-s3.credentials'
releaseConfig['S3Bucket']                   = 'net-mozaws-prod-delivery-archive'
releaseConfig['bouncerServer']              = 'download.mozilla.org'
releaseConfig['ausServerUrl']               = 'https://aus2-community.mozilla.org'
releaseConfig['candidatesPathName']         = 'candidates'
releaseConfig['testOlderPartials']          = False
releaseConfig['releaseNotesUrl']            = None
releaseConfig['releaseChannel']             = 'release'
releaseConfig['verifyConfigs']              = {
    'linux': 'mozEsr-seamonkey-linux.cfg',
    'macosx64': 'mozEsr-seamonkey-mac64.cfg',
    'win32': 'mozEsr-seamonkey-win32.cfg'
}
releaseConfig['mozconfigs']                 = {
    'linux': 'suite/config/mozconfigs/linux32/release',
    'linux64': 'suite/config/mozconfigs/linux64/release',
    'macosx64': 'suite/config/mozconfigs/macosx-universal/release',
    'win32': 'suite/config/mozconfigs/win32/release',
}

# Source step requires a properly configured source tree in order
# to upload the tarball.  re: bug 1118778
releaseConfig['source_mozconfig'] = 'suite/config/mozconfigs/linux64/source'

# Major update configuration
releaseConfig['majorUpdateRepoPath']        = None

# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'

# Mock
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux', 'linux64')

# Balrog Submission
releaseConfig['balrog_submit'] = True
