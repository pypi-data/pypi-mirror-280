# import os
# import sys
#
# def main():
#     from cbr_website_beta.cbr__flask.Flask_Site import Flask_Site
#     from osbot_utils.utils.Files import path_combine
#
#     path_to_add = path_combine(__file__, '..')     # this is needed to that the apps folder can be resolved
#     sys.path.append(path_to_add)
#
#     flask_site = Flask_Site()
#     app = flask_site.app()
#     port = int(os.environ.get("PORT", 3000))
#     app.run(host="0.0.0.0", port=port, debug=True)
#
# if __name__ == "__main__":
#     main()
import os

from cbr_website_beta import fast_api_main
app = fast_api_main.app
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port)