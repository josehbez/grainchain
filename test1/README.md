# FastAPI 

```bash
uvicorn app:app --reload --port 8022
```
## Requirements
<ol>
    <li>An additional application exists, named <i>Zeta</i>. It has an <i>API</i> thay you will use to get additional user information and validation. See <i>ZetaAPI.ipynb</i>, this notebook contains the information required in a running example.</li>
    <li>Endpoints must be developed to create, edit, and delete basic user information. You must include location, name, username, and a structure contain user information obtained from the <i>Zeta</i> application. See <i>MongoDB.ipynb</i>, this notebook contains the information required in a running example.</li>
    <li><u>Use the cells under the <b>FastAPI Start and Endpoint Tests</b> as guidance</u>, the expected endpoints and responses are already there.</li>
    <li>An endpoint must be developed to create 100 fake users, all fields must contain data and each user must be assigned to a random location.</li>
    <li>An endpoint must be developed to provide a report containing the amount of users linked to each location available, the count of user documents stored must be returned as well and the report must include at least ten faked locations.</li>
    <li><u>All tests in the <b>Task Testing</b> block must pass</u>.</li>
    <li><u>No previous users are expected on start</u>, the <i>MongoDB</i> collection must be empty. Feel free to create and use information as you see fit for your test, just take this in consideration for delivery purposes.</li>
</ol>