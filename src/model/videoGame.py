

class videoGame: 
    Rank=""
    Name=""
    Genre=""
    Platform=""
    Publisher=""
    Critic_score=""
    Img_url="https://www.vgchartz.com"
    
    
    def __init__(self, rank, name, genre, platform, publisher, critScore, imgUrl):
        super().__init__()
        
        self.Rank = rank
        self.Name = name
        self.Genre = genre
        self.Platform = platform
        self.Publisher = publisher
        self.Critic_score = critScore
        self.Img_url = self.Img_url + imgUrl
        
        
        
    def __repr__(self):
        return "Video Game: {},{},{},{},{},{},{}".format(self.Rank, self.Name, self.Genre,self.Platform,self.Publisher,self.Critic_score,self.Img_url)