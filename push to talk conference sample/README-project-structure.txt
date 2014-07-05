A b2bua-archetype project structure supports three kinds of code:

1) The E4SS app itself. ECharts (.ech) and java code go in src/main/ech and
   src/main/java. This code can be compiled with 'mvn compile' and packaged
   into a .sar file with 'mvn package'. Servlet configuration and other
   files (static html, jsps, etc...) to be packaged in the sar go in
   src/main/webapp.

2) KitCAT test code, to be executed against a deployed instance of the app, 
   goes in src/test/java. These test cases can be executed by running 
   'mvn ... verify'.  See README-testing.txt for more information on options 
   for automatic or manual deployment.

3) Test harness code for the KitCAT tests. If the E4SS app needs to be 
   extended to support testing (e.g., with additional servlets or jsps to be
   invoked by the KitCAT test code to change the app state), that code should
   be placed in src/testharness. When 'mvn package' is run, the resulting 
   test sar will include both the test harness code and the E4SS app code.
   The test sar will also include sip.xml and web.xml (and any other files)
   from src/testharness/webapp, rather than src/main/webapp.


