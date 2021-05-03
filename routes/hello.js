
let express = require('express')
let router = express.Router()

router.get('/',
    function(request, response) {
        h = "Hello world"
        response.status(200).send(h)
    }
);

module.exports = router;