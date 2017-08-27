{
  'variables': {
    'picohttpparser_base_cflags': [
      '-Wall',
      '-Wextra',
    ],

    'picohttpparser_debug_cflags': [
      '-g',
      '-O0',
    ],

    'picohttpparser_release_cflags': [
      '-O3',
    ],
  },

  'target_defaults': {
    'default_configuration': 'Release',

    'configurations': {
      'Debug': {
        'cflags': ['<@(picohttpparser_debug_cflags)'],
        'xcode_settings': {
          'OTHER_CFLAGS': ['<@(picohttpparser_debug_cflags)'],
        },
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1,  # static debug
          },
        },
      },

      'Release': {
        'cflags': ['<@(picohttpparser_release_cflags)'],
        'xcode_settings': {
          'OTHER_CFLAGS': ['<@(picohttpparser_release_cflags)'],
        },
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0,  # static release
          },
        },
      },
    },

    'cflags': ['<@(picohttpparser_base_cflags)'],
    'xcode_settings': {
      'OTHER_CFLAGS': ['<@(picohttpparser_base_cflags)'],
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },

    'conditions': [
      ['OS == "win"', {
        'defines': [
          'WIN32',
        ],
      }],
    ],

    'include_dirs': ['.'],
    'sources': [
      'picohttpparser.c',
      'picohttpparser.h',
    ],
  },

  'targets': [
    {
      'target_name': 'picohttpparser',
      'type': 'static_library',
    },

    {
      'target_name': 'picohttpparser-test',
      'type': 'executable',
      'sources': [
        'test.c',
        'picotest/picotest.c',
        'picotest/picotest.h',
      ],
    },

    {
      'target_name': 'picohttpparser-bench',
      'type': 'executable',
      'sources': [
        'bench.c',
      ],
    },
  ],
}
