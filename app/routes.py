from flask import Blueprint, render_template

main = Blueprint('main', __name__)

HOME_CARDS = [
    {
        'id': 'Taylor-AI',
        'badge': 'Popular',
        'title': 'TaylorAI',
        'description': 'Got questions? Get instant answers - Ask AI to analyse your data and uncover insights',
        'route': 'AI-Tools'
    },
    {
        'id': 'view-reports',
        'badge': 'Trending',
        'title': 'View Reports, MI, and Analytics',
        'description': 'Access dashboards, performance metrics, and MI reports to track progress and make informed decisions.',
        'route': 'insights-reporting'
    },
    {
        'id': 'exploration-analytics',
        'badge': 'Popular',
        'title': 'Exploration & Analytics',
        'description': 'Utilise advanced tools and models, such as predictive analytics and AI, to unlock deeper insights.',
        'route': 'exploration-analytics'
    },
    {
        'id': 'reports-create',
        'badge': 'Popular',
        'title': 'Reports, MI, Create your own Report',
        'description': 'Create Power BI Reports using AI Tools',
        'route': 'insights-reporting'
    },
    {
        'id': 'unstructured-data-upload',
        'badge': 'Recommended',
        'title': 'Semi & Unstructured data upload',
        'description': 'Turn data into insights effortlessly—create tailored reports with our ready-to-use Power BI models.',
        'route': 'insights-reporting'
    },
    {
        'id': 'data-collaboration',
        'badge': 'Recommended',
        'title': 'Data Collaboration',
        'description': 'Deliver the right data to the right people—reporting that\'s built for collaboration, not just consumption.',
        'route': 'insights-reporting'
    }
]

MOCK_REPORTS = {
    'buyer-analysis': {
        'title': 'Buyer Analysis Report',
        'description': 'Comprehensive analysis of buyer demographics, behavior patterns, and market trends',
        'metrics': [
            {'label': 'Total Buyers', 'value': '2,847', 'change': '+12%'},
            {'label': 'First-Time Buyers', 'value': '62%', 'change': '+5%'},
            {'label': 'Avg. Completion Time', 'value': '89 days', 'change': '-7%'},
            {'label': 'Customer Satisfaction', 'value': '4.6/5', 'change': '+0.3'}
        ],
        'insights': [
            'First-time buyers increased by 15% this quarter',
            'Solicitor-driven delays decreased by 23%',
            'Peak buying season identified: March-May',
            'Digital engagement up 45% year-over-year'
        ],
        'chart_data': {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'values': [234, 267, 312, 289, 301, 276]
        }
    },
    'risk-analysis': {
        'title': 'Project Risk Analysis Report',
        'description': 'Predictive analytics for identifying and mitigating project risks across all developments',
        'metrics': [
            {'label': 'Active Projects', 'value': '47', 'change': '+3'},
            {'label': 'High Risk Projects', 'value': '8', 'change': '-2'},
            {'label': 'Budget Variance', 'value': '3.2%', 'change': '+1.1%'},
            {'label': 'On-Time Delivery', 'value': '83%', 'change': '+5%'}
        ],
        'insights': [
            'Supply chain delays affecting 12% of projects',
            'Weather-related risks down 40% with new protocols',
            'Resource allocation improved by 18%',
            'Early warning system prevented 5 major delays'
        ],
        'chart_data': {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'values': [12, 10, 8, 9, 7, 8]
        }
    },
    'plot-analysis': {
        'title': 'Plot Analysis Report',
        'description': 'Detailed analysis of plot performance, availability, and sales velocity',
        'metrics': [
            {'label': 'Total Plots', 'value': '1,243', 'change': '+45'},
            {'label': 'Available Plots', 'value': '387', 'change': '-89'},
            {'label': 'Avg. Sale Time', 'value': '42 days', 'change': '-5 days'},
            {'label': 'Sales Velocity', 'value': '2.8/week', 'change': '+0.6'}
        ],
        'insights': [
            'Premium plots selling 30% faster than standard',
            'Corner plots have 25% higher demand',
            'South-facing plots command 8% price premium',
            'Garden size is top buyer priority (67%)'
        ],
        'chart_data': {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'values': [156, 178, 189, 201, 223, 195]
        }
    },
    'sales-insights': {
        'title': 'Sales Insights Report',
        'description': 'Comprehensive sales performance tracking and conversion rate analysis',
        'metrics': [
            {'label': 'Total Sales', 'value': '£47.2M', 'change': '+18%'},
            {'label': 'Conversion Rate', 'value': '34%', 'change': '+4%'},
            {'label': 'Avg. Sale Price', 'value': '£385K', 'change': '+6%'},
            {'label': 'Pipeline Value', 'value': '£89.3M', 'change': '+22%'}
        ],
        'insights': [
            'Q2 sales exceeded targets by 15%',
            'Digital leads converting 40% better',
            'Weekend viewings generate 2x bookings',
            'Email campaigns showing 28% open rate'
        ],
        'chart_data': {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'values': [6.8, 7.2, 8.1, 7.9, 8.4, 8.8]
        }
    }
}

EXPLORER_SECTIONS = {
    'exploration-analytics': {
        'title': 'Exploration & Analytics',
        'items': [
            {
                'title': 'Buyer Analysis',
                'description': 'Discover who\'s buying and how—unlock insights on first-time buyers, buying patterns, and solicitor-driven timelines to sharpen your marketing strategy.',
                'image': 'buyer-analysis.jpg',
                'color': 'dark',
                'report_id': 'buyer-analysis'
            },
            {
                'title': 'Project Risk Analysis',
                'description': 'Leverage predictive analytics to assess potential risks across projects, including delays, budget overruns, and resource constraints for proactive decision-making.',
                'image': 'risk-analysis.jpg',
                'color': 'gradient',
                'report_id': 'risk-analysis'
            },
            {
                'title': 'Plot Analysis',
                'description': 'Analyze plot performance, availability, and sales velocity across developments to optimize pricing and inventory management strategies.',
                'image': 'plot-analysis.jpg',
                'color': 'light',
                'report_id': 'plot-analysis'
            },
            {
                'title': 'Sales Insights',
                'description': 'Track sales performance, conversion rates, and revenue trends to identify opportunities and drive strategic sales initiatives.',
                'image': 'sales-insights.jpg',
                'color': 'dark',
                'report_id': 'sales-insights'
            }
        ]
    },
    'insights-reporting': {
        'title': 'Insights & Reporting',
        'items': [
            {
                'title': 'Executive Dashboards',
                'description': 'Access high-level dashboards with key performance indicators and strategic metrics.',
                'image': 'dashboards.jpg',
                'color': 'gradient',
                'report_id': None
            },
            {
                'title': 'Custom Reports',
                'description': 'Generate detailed reports tailored to your specific business requirements and KPIs.',
                'image': 'reports.jpg',
                'color': 'dark',
                'report_id': None
            }
        ]
    }
}


@main.route('/')
def home():
    return render_template('home.html', cards=HOME_CARDS)


@main.route('/explorer/<section>')
def explorer(section):
    section_data = EXPLORER_SECTIONS.get(section)
    if not section_data:
        return render_template('404.html'), 404

    tabs = [
        {'id': 'exploration-analytics', 'name': 'Exploration & Analytics'},
        {'id': 'insights-reporting', 'name': 'Insights & Reporting'}
    ]

    return render_template('explorer.html', 
                         section=section_data,
                         current_section=section,
                         tabs=tabs)


@main.route('/report/<report_id>')
def report(report_id):
    report_data = MOCK_REPORTS.get(report_id)
    
    if not report_data:
        return render_template('404.html'), 404
    
    return render_template('report_poc.html', 
                         report=report_data,
                         report_id=report_id)