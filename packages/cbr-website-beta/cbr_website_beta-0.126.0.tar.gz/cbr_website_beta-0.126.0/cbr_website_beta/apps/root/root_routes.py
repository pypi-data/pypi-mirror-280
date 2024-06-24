from flask                                                      import render_template, redirect, Response
from cbr_website_beta.config.CBR_Config                         import cbr_config, CBR_Config
from cbr_website_beta.apps.llms.Initial_Message                 import Initial_Message
from cbr_website_beta.apps.llms.Prompt_Examples                 import Prompt_Examples
from cbr_website_beta.apps.llms.System_Prompt                   import System_Prompt
from cbr_website_beta.apps.llms.llms_routes                     import user_data_for_prompt, current_user_data
from cbr_website_beta.apps.root                                 import blueprint
from cbr_website_beta.apps.user.user_profile                    import render_page__login_required
from cbr_website_beta.cbr__flask.decorators.allow_annonymous    import allow_anonymous
from cbr_website_beta.config.CBR__Site_Info                     import cbr_site_info
from cbr_website_beta.utils.Version                             import Version


@blueprint.route('/version')
@allow_anonymous
def version():
    version = Version().value()         # get this value dynamically (which useful in some live customisation and debugging sessions)
    return Response(version, content_type='text/plain')

@blueprint.route('/home')
@blueprint.route('/home.html')
@allow_anonymous
def home():
    user_data       = current_user_data()
    title           = 'Welcome'
    first_name      = user_data.get('First name','')
    last_name       = user_data.get('Last name' ,'')
    content_view    = 'includes/home.html'

    template_name = '/pages/page_with_view.html'
    return render_template(template_name_or_list = template_name,
                           title                 =  title       ,
                           content_view          = content_view ,
                           first_name            = first_name   ,
                           last_name             = last_name    )


@blueprint.route('/athena')
@allow_anonymous
def athena():
    user_data = user_data_for_prompt()
    title     = 'Athena'
    if user_data or cbr_config.login_disabled():
        url_athena       = cbr_site_info.target_athena_url() + '/open_ai/prompt_with_system__stream'  # todo: refactor into helper method
        content_view     = '/llms/open_ai/chat_bot_ui.html'
        template_name    = '/pages/page_with_view.html'
        examples_title   = 'Prompt examples'

        return render_template( template_name_or_list = template_name               ,
                                content_view          = content_view                ,
                                examples_texts        = Prompt_Examples().athena()  ,        # todo: refactor to not need to call Prompt_Examples() on all calls
                                examples_title        = examples_title              ,
                                initial_message       = Initial_Message().athena()  ,         # todo: refactor to not need to call Prompt_Examples() on all calls
                                system_prompt         = System_Prompt().athena()    ,
                                title                 = title                       ,
                                url_athena            = url_athena                  ,
                                user_data             = user_data                   )
    else:
        return render_page__login_required(title)

########### llms-chat ###########

@blueprint.route('/chat-with-llms')
@allow_anonymous
def llms_chat():
    url_athena       = cbr_site_info.target_athena_url() + '/open_ai/prompt_with_system__stream'
    title            = "Chat with Multiple LLMs (with no system prompt)"
    content_view     = '/llms/chat_with_llms/no-prompt.html'
    template_name    = '/pages/page_with_view.html'
    examples_title   = 'Prompt examples'

    return render_template( template_name_or_list = template_name                       ,
                            content_view          = content_view                        ,
                            examples_texts        = Prompt_Examples().chat_with_llms()  ,        # todo: refactor to not need to call Prompt_Examples() on all calls
                            examples_title        = examples_title                      ,
                            url_athena            = url_athena                          ,
                            initial_message       = Initial_Message().chat_with_llms()  ,         # todo: refactor to not need to call Prompt_Examples() on all calls
                            title                 = title                               )