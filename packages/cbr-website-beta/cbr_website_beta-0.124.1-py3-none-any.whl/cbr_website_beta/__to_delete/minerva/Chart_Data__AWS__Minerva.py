# from cbr_website_beta.bots.Minerva_Rest_API import Minerva_Rest_API
#
# SERVICES_TO_SKIP = ['Amazon Registrar', 'Tax', 'Refund', 'AWS Key Management Service', 'Amazon Relational Database Service',
#                     'AWS CloudTrail','AmazonCloudWatch','AWS Secrets Manager',
#                     'Amazon Virtual Private Cloud','Amazon Virtual Private Cloud',
#                     'Amazon Simple Notification Service','AWS Step Functions',
#                     'Amazon Route 53',
#                     #'Amazon API Gateway', 'Amazon EC2 Container Registry (ECR)'
#                     ]
#
# class Chart_Data__AWS__Minerva:
#
#     def __init__(self):
#         self.bot_minerva       = Minerva_Rest_API()
#
#     def aws_cost_explorer(self):
#         cost_data    = self.bot_minerva.aws_cost_explorer()
#         indexed_data = {}
#
#         for day, services in cost_data.items():
#             for service, info in services.items():
#                 if service in SERVICES_TO_SKIP:
#                     continue
#                 if service not in indexed_data:
#                     indexed_data[service] = {}
#
#                 indexed_data[service][day] = {'cost': info['cost']}
#
#         all_services = list(indexed_data.keys())
#         all_days    = list(cost_data.keys())
#
#         all_costs = []
#         for service in all_services:
#             day_data = []
#             for day in all_days:
#                 if day not in indexed_data.get(service):
#                     value = 0
#                 else:
#                     value = indexed_data[service][day]['cost']
#                 day_data.append(value)
#             all_costs.append(day_data)
#
#
#         chart_data= dict(all_services=all_services,
#                          all_days=all_days,
#                          all_costs=all_costs)
#         return chart_data

# ROUTE CODE

# # todo: fix this route when minerva is fixed (also add caching layer to minerva since there
# #       is no point of making more than one call per 8 hours)
# @blueprint.route('/aws-costs')
# def aws_costs():
#     # chart_data = Chart_Data__AWS__Minerva().aws_cost_explorer()
#     # chart_labels = chart_data.get('all_days')
#     # chart_series = chart_data.get('all_costs')
#     # all_services = chart_data.get('all_services')
#     chart_labels = {}
#     chart_series = {}
#     all_services = {}
#     return render_template('minerva/aws-costs.html',
#                            chart_labels=chart_labels,
#                            chart_series=chart_series,
#                            all_services=all_services)