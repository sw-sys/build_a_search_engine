# Google Programmable Search Engine

## Instructions

1. Go to https://programmablesearchengine.google.com/
2. Select 'Add'
3. Fill in the details for the websites you want to search
4. Click 'create'
5. You can retrieve search results using the API - scroll to the bottom of the page, look for the 'Programmatic access' section
6. Select 'Get started'
7. Select 'Get a Key' button
8. Create an .env file & add this key as the 'KEY =' value
9. Also add the 'CX_ENGINE' value to the .env (this is your 'Search Engine ID' - click on your search engine's name from this webpage andy ou should see it https://programmablesearchengine.google.com/controlpanel/all)

## About

- The API responds in JSON.
- The output will be in CSV, and the file named using the date, time and keywords used to retrieve the results.
- The output will be 10 results (you can set this from 1 to 10 with the 'num' param)
- The API can output up to 100 results but you'd need to change the 'start' param value e.g. 11 would take you to the start of page two, as results are paginated in 10s - as the Google Custom Search UI is. See the 'Google custom search' docs (below) for more info.

## Important

If you put a keyword in q (for query) and then put a keyword in 'hq', the two works will be combined with the logical AND operator

# Docs

- Google Custom Search docs https://developers.google.com/custom-search/v1/introduction
- requests docs https://requests.readthedocs.io/en/latest/user/quickstart/

## PARAM VALUES

- c2coff values (1 disable 0 on)
- cd filter values https://developers.google.com/custom-search/docs/json_api_reference#countryCollections
- filetype values https://developers.google.com/search/docs/crawling-indexing/indexable-file-types?visit_id=638781849619369383-3223422633&rd=1
- gl filter values https://developers.google.com/custom-search/docs/json_api_reference#countryCodes
- hl values https://developers.google.com/custom-search/docs/json_api_reference#wsInterfaceLanguages
- rights values (cc_publicdomain, cc_attribute, cc_sharealike, cc_noncommercial, cc_nonderived etc) https://wiki.creativecommons.org/wiki/CC_Search_integration
- safe values ('active' or 'off')
- sort https://developers.google.com/custom-search/docs/structured_search#sort-by-attribute
