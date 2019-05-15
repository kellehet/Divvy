
const search = instantsearch({
  indexName: 'Dividend',
  searchClient: algoliasearch('RMWLJARDE4', 'fd35ec2f71ec237e60b38cb7b8788deb'),
});

search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-box',
  })
);

search.addWidget(
  instantsearch.widgets.clearRefinements({
    container: '#clear-refinements',
  })
);

search.addWidget(
  instantsearch.widgets.refinementList({
    container: '#sector-list',
    attribute: 'sector',
  })
);
search.addWidget(
  instantsearch.widgets.refinementList({
    container: '#industry-list',
    attribute: 'industry',
  })
);

search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: `
        <div>

          <div class="hit-name">
            {{#helpers.highlight}}{ "attribute": "company" }{{/helpers.highlight}}
          </div>
          <div class="hit-description">
            {{#helpers.highlight}}{ "attribute": "symbol" }{{/helpers.highlight}}
          </div>
          <div class="hit-price">\${{price}}</div>
        </div>
      `,
    },
  })
);

search.addWidget(
  instantsearch.widgets.rangeSlider({
    container: '#range-slider',
    attribute: 'div_yield',
  })
);
search.addWidget(
instantsearch.widgets.numericMenu({
  container: '#numeric-menu',
  attribute: 'cons_years',
  items: [
    { label: 'All' },
    { label: 'Less than 10', end: 10 },
    { label: 'Between 10 - 25', start: 10, end: 25 },
    { label: 'More than 25', start: 25 },
  ],
}));

search.addWidget(
  instantsearch.widgets.pagination({
    container: '#pagination',
  })
);


search.start();
