from osbot_utils.base_classes.Type_Safe import Type_Safe


class LLMs__Platforms(Type_Safe):

    def model_options(self):
        return { 'OpenAI (Paid)'     : { 'OpenAI'       : { '1. GPT 4o'           : 'gpt-4o'                              ,
                                                            '2. GPT 4 Turbo'      : 'gpt-4-turbo'                         ,
                                                            '3. GPT 3.5 Turbo'    : 'gpt-3.5-turbo'                       }},
                 'Grog (Free)'       : { 'Meta'         : { 'LLaMA3 8b'        : 'llama3-8b-8192'                      ,
                                                            'LLaMA3 70b'       : 'llama3-70b-8192'                      },
                                         'Mistral'      : { 'Mixtral 8x7b'     : 'mixtral-8x7b-32768'                  },
                                         'Google'       : { 'Gemma 7b'         : 'gemma-7b-it'                         }},
                 'Open Router (Free)': { 'Google'       : { 'Gemma 7b'         : 'google/gemma-7b-it:free'             },
                                         'Meta'         : { 'LLaMA3 8b'        : 'meta-llama/llama-3-8b-instruct:free' },
                                         'Nous Research': { 'Capybara 7b'      : 'nousresearch/nous-capybara-7b:free'  },
                                         'Open Chat'    : { 'Openchat 7b'      : 'openchat/openchat-7b:free'           },
                                         'Gryphe'       : { 'Mythomist 7b'     : 'gryphe/mythomist-7b:free'            },
                                         'Undi 95'      : { 'Toppy M 7b'       :  'undi95/toppy-m-7b:free'             },
                                         'Open Router'  : { 'Cinematika 7b'    : 'openrouter/cinematika-7b:free'       },
                                         'jetmoe'       : {' jetmoe-8b'        :  'jetmoe/jetmoe-8b-chat:free'         }},
                 'Open Router (Paid)': { 'Google'       : { 'Gemini Flash 1.5' : 'google/gemini-flash-1.5'             }}}


