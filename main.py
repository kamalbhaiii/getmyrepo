from fastapi import FastAPI, Response, status
import Scrap

app = FastAPI()

repos = Scrap.Scrap

@app.get("/", status_code="200")
async def root(response : Response):
    response.status_code = status.HTTP_200_OK
    return {
        'greet':"Welcome to Get My Repo API",
        'description':"This API can be used to scrap the 'star' marked 'public' github repository.",
        'how-to-use':{
            'answer':"Just add the username of your Github Account as shown in example below.",
            'example':"https://getmyrepo.deta.dev/{USERNAME}"
        },
        'note':"'Star' mark those repositories on your github account which you want to scrap.",
        'message-from-admin':"Thank You for using this API, I am Kamal Sharma an undergraduate student from Gujarat Technological University, India.Use this API wisely and for any suggestions reach me by doing e-mail. Happy Hacking!!",
        'admin-email':"kamal5201ks@gmail.com",

    }

@app.get("/{user}", status_code=200)
async def repo(user : str,response: Response):
    response.status_code = status.HTTP_200_OK
    return repos.scrapRepo(user)