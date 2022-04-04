# Draw-a-heart-shape
*Note, you may download the entire code (turtle.py) in the 'master' branch.

Turtle is a cute and amazing library in python. Let's draw a heart shape with turtle. This will be my very first project here.

Drawing a heart shape is not something new. There are lots of exsiting code for referring (e.g. [geeks for geeks](https://www.geeksforgeeks.org/draw-heart-using-turtle-graphics-in-python)) However, when checking such example codes, my concern is that how did they get such precise parameters? It's not very intuitive. So this project is a simple version of deriving the parameters:

- started form the bottom, draw a line which forms a 45 degree angle with positive x-axis.
<img width="478" alt="image" src="https://user-images.githubusercontent.com/99280254/161413669-66cc52d7-b02f-445e-a16f-6a74f4a819d6.png">

- the upper part is an arc, so for each move, we could turn right for one single degree. Moving forward for 180 degree, we will get a semicircle. But what is the perimeter of this semicircle? Let's derive with basic geometry. If the length of the straight line is 135, then the length of the semicircle would be 720/3.14 approximately.
<img width="650" alt="image" src="https://user-images.githubusercontent.com/99280254/161425874-967f8c77-4ee4-45af-9fac-b3427afed727.png">

- Now repeat the steps for the right-hand side with merely changing the directions.
<img width="558" alt="image" src="https://user-images.githubusercontent.com/99280254/161425884-726fd6d4-68db-4255-b067-119557105ef1.png">

The detailed code is shown in turtle.py

p.s.
[Click here to check the Chinese version](https://mp.weixin.qq.com/s/LvtHLaN31_LEnBhbL5tA1g)
