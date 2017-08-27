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

    'picohttpparser_sse_cflags': [
      '-msse4.2',
    ],

    'picohttpparser_sources': [
      'picohttpparser.c',
      'picohttpparser.h',
    ],

    'picohttpparser_test_sources': [
      'test.c',
      'picohttpparser.h',
      'picotest/picotest.c',
      'picotest/picotest.h',
    ],

    'picohttpparser_bench_sources': [
      'bench.c',
      'picohttpparser.h',
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
  },

  'targets': [
    {
      'target_name': 'picohttpparser',
      'type': 'static_library',
      'sources': ['<@(picohttpparser_sources)'],
    },

    {
      'target_name': 'picohttpparser-sse4.2',
      'type': 'static_library',
      'defines': [
        '__SSE4_2__=1',
      ],
      'cflags': ['<@(picohttpparser_sse_cflags)'],
      'xcode_settings': {
        'OTHER_CFLAGS': ['<@(picohttpparser_sse_cflags)'],
      },
      'sources': ['<@(picohttpparser_sources)'],
    },

    {
      'target_name': 'picohttpparser-test',
      'type': 'executable',
      'dependencies': ['picohttpparser'],
      'sources': ['<@(picohttpparser_test_sources)'],
    },

    {
      'target_name': 'picohttpparser-sse4.2-test',
      'type': 'executable',
      'dependencies': ['picohttpparser-sse4.2'],
      'sources': ['<@(picohttpparser_test_sources)'],
    },

    {
      'target_name': 'picohttpparser-bench',
      'type': 'executable',
      'dependencies': ['picohttpparser'],
      'sources': ['<@(picohttpparser_bench_sources)'],
    },

    {
      'target_name': 'picohttpparser-sse4.2-bench',
      'type': 'executable',
      'dependencies': ['picohttpparser-sse4.2'],
      'sources': ['<@(picohttpparser_bench_sources)'],
    },
  ],
}
