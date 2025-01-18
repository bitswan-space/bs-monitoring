const config = {
  title: 'Bs Monitoring',
  tagline: 'Bs Monitoring',
  favicon: 'img/logo.svg',
  url: 'https://bitswan-space.github.io',
  baseUrl: '/bs-monitoring/',
  organizationName: 'bitswan-space',
  projectName: 'bsmonitoring',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          editUrl: 'https://github.com/bitswan-space/bsmonitoring/tree/main/docs/',
          routeBasePath: '/',
          path: 'docs',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Bs Monitoring',
      logo: {
        alt: 'Project Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Docs',
        },
        {
          href: 'https://github.com/bitswan-space/bs-monitoring',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Overview',
              to: '/overview/introduction',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/bitswan-space/bs-monitoring',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Bs Monitoring. Built with Docusaurus.`,
    },
  },
};

module.exports = config; 
