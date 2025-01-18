const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Overview',
      items: [
        'overview/introduction',
        'overview/installation',
        'overview/configuration',
        'overview/custom_modules',
        'overview/example',
      ],
    },
    {
      type: 'category',
      label: 'Data Sources',
      items: [
        'datasources/introduction',
        'datasources/elastic'
      ],
    },
    {
      type: 'category',
      label: 'Alert Services',
      items: [
        'alertservices/introduction',
        'alertservices/discord',
        'alertservices/opsgenie',
      ],
    },
    {
      type: 'category',
      label: 'Monitors',
      items: [
        'monitors/introduction',
        'monitors/data_quantity',
        'monitors/data_scheme',
      ],
    },
    {
      type: 'category',
      label: 'Databases',
      items: [
        'databases/introduction',
        'databases/postgres',
        'databases/sqlite',
      ],
    },
  ],
};

module.exports = sidebars; 
