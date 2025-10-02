from flask import Blueprint, render_template

main = Blueprint('main', __name__)

HOME_CARDS = [
    {
        'id': 'Taylor-AI',
        # primary badge as string (templates expect a string so .lower() works)
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
        'route': 'insights-reporting'
    },
    {
        'id': 'reports-create',
        'badge': 'Popular',
        'title': 'Reports, MI, Create your own Report',
        'description': 'Create Power BI Reports using AI Tools',
        'route': ['insights-reporting', 'AI-Tools']
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
        'description': 'Deliver the right data to the right people—reporting that’s built for collaboration, not just consumption.',
        'route': 'insights-reporting'
    }
]

EXPLORER_SECTIONS = {
    'Exploration & Analytics': {
        'title': 'Buyer Analysis',
        'items': [
            {
                'title': 'Buyer Analysis',
                'description': 'Discover who\'s buying and how—unlock insights on first-time buyers, buying patterns, and solicitor-driven timelines to sharpen your marketing strategy. Predict completion times, spot risks early, and understand your buyers like never before—click to explore the intelligence behind every purchase.',
                'image': 'BAnalysis.jpg',
                'color': 'dark'
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
        {'id': 'exploration-analytics', 'name': 'Exploration & Analytics'}
    ]

    return render_template('explorer.html', section=section_data, current_section=section, tabs=tabs)
