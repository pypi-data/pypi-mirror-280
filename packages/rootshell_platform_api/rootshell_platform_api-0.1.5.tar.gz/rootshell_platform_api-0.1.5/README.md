
A project to access Rootshell's Public API. 

`pip install rootshell_platform_api`

The `BEARER_TOKEN` can be accessed in the Platform. 
The `API_ENDPOINT` is the tenant url which you want access the data.
```shell
export BEARER_TOKEN=your_token_here
export API_ENDPOINT=https://your.api.endpoint
```

Currently list of groups that are accessible

```text
tags
    get-paginated
    get-single
    create
    update
    delete
projects
    get-paginated
    get-single
    create
    update
    delete
```
Example:
```shell
rootshell_platform tags get_paginated
```

