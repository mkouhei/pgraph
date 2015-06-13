$(function(){
   $("#graph").linkDraw({
     "configPath": "/api/linkdraw/py-deps/0.2.0",
     "positionPath": "positions/py-deps.json", 
     "positionWriter": "api/positions",
     "positionSave": false,
     //"zoom": false,
     //"drag": false,
     "width": 800,
     "height": 600,
     "interval":0
   });
});
