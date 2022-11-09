# CaboCha on Flask

A CaboCha processor through Web GUI.

# How to Install
````
 % docker --name cabocha_on_flask build .
````
# How to Run
````
 % docker run --name cof --net=host -v $(pwd):/root/workspace -it cabocha_on_flask "python /root/workspace/app.py"
````
Then, access to `http://localhost:5000`
