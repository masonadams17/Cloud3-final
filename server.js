const Express = require ('express');
const helloRoute = require('./routes/hello');


//Creates the Express application
const app = Express()

//Maps the /hello route to the hello.js file 
app.use('/hello', helloRoute)



app.listen(8080, ()=>console.log("Server listening on port 8080 ..."));