## About the connector
Google Dorking refers to the practice of using advanced search operators in Google's search engine to discover information that may not be readily accessible through conventional search queries.
<p>This document provides information about the Google Dorking Connector, which facilitates automated interactions, with a Google Dorking server using FortiSOAR&trade; playbooks. Add the Google Dorking Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Google Dorking.</p>

### Version information

Connector Version: 1.0.0

FortiSOAR&trade; Version Tested on: 7.5.0-4015

Google Dorking API Version Tested on: v1

Authored By: Fortinet

Certified: Yes

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-google-dorking</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Google Dorking server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Google Dorking server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Google Dorking</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Google Dorking server to connect and perform automated operations.
</td>
</tr><tr><td>API Key</td><td>Specify the API key to access the endpoint to connect and perform the automated operations
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Custom Search</td><td>A custom search refers to the ability to create a personalized search engine tailored to the specific needs of a website's audience, providing a customized and efficient way for users to find content within a website.</td><td>custom_search <br/>Investigation</td></tr>
</tbody></table>

### operation: Custom Search
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search Engine ID</td><td>Specify the Programmable Search Engine you want to use to perform this search. The search engine must be created with the Control Panel Note: The Search Engine ID (cx) can be of different format (e.g. 8ac1ab64606d234f1)
</td></tr><tr><td>Search Query</td><td>A search query refers to the text or keywords entered by a user into a search engine when they are looking for information, documents, websites, or any other content.
</td></tr><tr><td>Include Phrase</td><td>Specify a word or phrase that all documents in the search results must contain.
</td></tr><tr><td>Exclude Phrase</td><td>Specify a word or phrase that should not appear in any documents in the search results.
</td></tr><tr><td>Safe Search</td><td>Select to enable the SafeSearch filtering. By default, this is set to false.
</td></tr><tr><td>Count</td><td>Specify the maximum count of records that you want this operation to fetch from Google Dorking. By default, this option is set to 10, and valid values are integers between 1 and 10.
</td></tr><tr><td>Start</td><td>Specify the index of the first result to return. The default number of results per page is 10, so &start=11 would start at the top of the second page of results. Note: The JSON API will never return more than 100 results, even if more than 100 documents match the query, so setting the sum of start + count to a number greater than 100 will produce an error. Also note that the maximum value for count is 10.
</td></tr><tr><td>Additional Fields</td><td>Additional fields, in the JSON format, based on which you want to retrieve details from Google Dorking. For reference, you can refer this link https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list#request
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "kind": "",
    "url": {
        "type": "",
        "template": ""
    },
    "queries": {
        "previousPage": [
            {
                "title": "",
                "totalResults": "",
                "searchTerms": "",
                "count": "",
                "startIndex": "",
                "inputEncoding": "",
                "outputEncoding": "",
                "safe": "",
                "cx": ""
            }
        ],
        "request": [
            {
                "title": "",
                "totalResults": "",
                "searchTerms": "",
                "count": "",
                "startIndex": "",
                "inputEncoding": "",
                "outputEncoding": "",
                "safe": "",
                "cx": ""
            }
        ],
        "nextPage": [
            {
                "title": "",
                "totalResults": "",
                "searchTerms": "",
                "count": "",
                "startIndex": "",
                "inputEncoding": "",
                "outputEncoding": "",
                "safe": "",
                "cx": ""
            }
        ]
    },
    "context": {
        "title": "",
        "facets": [
            [
                {
                    "anchor": "",
                    "label": "",
                    "label_with_op": ""
                }
            ]
        ]
    },
    "searchInformation": {
        "searchTime": "",
        "formattedSearchTime": "",
        "totalResults": "",
        "formattedTotalResults": ""
    },
    "items": [
        {
            "kind": "",
            "title": "",
            "htmlTitle": "",
            "link": "",
            "displayLink": "",
            "snippet": "",
            "htmlSnippet": "",
            "cacheId": "",
            "formattedUrl": "",
            "htmlFormattedUrl": ""
        }
    ]
}</pre>
## Included playbooks
The `Sample - Google Dorking - 1.0.0` playbook collection comes bundled with the Google Dorking connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Google Dorking connector.

- Custom Search

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
