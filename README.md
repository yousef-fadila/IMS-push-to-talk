Push To Talk application server. 
================================

This software written by Yousef Fadila/Chen Flisher as a final project in IMS application servers development course using E4SS framework. 

To read more about E4SS, Please follow this link

[http://echarts.org/ECharts-for-SIP-Servlets/][1] 

Compiling & running
==============================

You need to have echarts compiler installed in your machine to compile the ech files into java files. 
After compiling, you can deploy to any container support sip servlets.
Tomcat with mobicents will works well for this purpose.

[http://www.mobicents.org/installation-tomcat.html][2] 

after deploying the server, you can connect to it using any SIP client, In the demo we have used the kapanga softphone.

[http://www.kapanga.net/IP/home.cfm][3] 

After connecting, use 1 to get talk permission and 2 to release and allow others to get the talk permission. This solution is 1 talking, other listing, so you need to release to allow others take the talk permissions 

A real push-to-talk conference with one button can be implemented as sending DTMF 1 when pressing the talk button, sending DTMF 2 once the talk button is released.

The software has also a web control client that allows kick-off members/ showing who is talking now and other basic features. The web client was introduced to show how http and sip can live together.

Screenshots:
==================
![image alt][4]

![image alt][5]
![image alt][6]
![image alt][7]


  [1]: http://echarts.org/ECharts-for-SIP-Servlets/
  [2]: http://www.mobicents.org/installation-tomcat.html
  [3]: http://www.kapanga.net/IP/home.cfm
  [4]: https://raw.githubusercontent.com/yousef-fadila/IMS-push-to-talk/master/arch.png
  [5]: https://raw.githubusercontent.com/yousef-fadila/IMS-push-to-talk/master/web-control-page.png
  [6]: https://raw.githubusercontent.com/yousef-fadila/IMS-push-to-talk/master/initialcallflow.png
  [7]: https://raw.githubusercontent.com/yousef-fadila/IMS-push-to-talk/master/push-to-tlak-flow.png