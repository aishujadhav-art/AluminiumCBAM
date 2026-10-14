# Aluminium CBAM Calculator

A free, browser based tool to estimate the carbon cost on the aluminium sheet a company buys: EU CBAM, UK CBAM from 2027, and the carbon price already built into metal made in Europe (EU ETS) or the UK (UK ETS).

What it does:

1. Inputs: where your company imports into (an EU country, the UK or any other country), volumes, aluminium mix and where each supply chain's metal is made. Every value can be your own or a sourced default.
2. Results: total carbon cost and CBAM only, per tonne and in total, year by year over 10 years, for up to five supply chains, with every calculation step shown.
3. Supply mix: split purchases across supply chains and countries, see the blended cost, which supplier drives it and ways to cut it, and compare countries under EU default values.
4. Low emission switch: plan a move to recycled or low carbon aluminium and see the saving.

Live data:

1. Exchange rates (euro and pound against the US dollar) load from the European Central Bank, through the free Frankfurter API, every time the page opens.
2. The EU CBAM certificate price is read from the European Commission's published quarterly prices once a week by a GitHub Action (.github/workflows/update-prices.yml), which saves it to prices.json. The page loads prices.json when it opens.
3. EU ETS and UK ETS market prices have no free official API, so they are entered defaults with sources and can be changed by the user.

Everything runs in your browser. No data is sent anywhere; inputs are kept only in your own browser.

Rules, benchmarks and prices were last checked on 14 October 2026. See the "Method" page in the tool for every formula and source.

This tool gives estimates only. It is not legal, tax or customs advice.
