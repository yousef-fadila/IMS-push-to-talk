
// $Name:  $ $Id: $

package att.com.ConferenceSample;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.MalformedURLException;
import java.net.URLEncoder;
import java.util.Formatter;
import java.util.Locale;
import java.util.Properties;

import org.echarts.test.sip.*;

import org.apache.log4j.Logger;

import org.junit.After;
import org.junit.Before;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test; //Import Before, Test, After annotations
import org.junit.Ignore;

import static org.echarts.test.sip.CATMatchers.*;
import static org.hamcrest.Matchers.*;

import com.gargoylesoftware.htmlunit.FailingHttpStatusCodeException;
import com.gargoylesoftware.htmlunit.WebClient;

public final class ConferenceSampleMachineTest extends org.echarts.test.sip.CATTestCase {
    /** Version control identifier strings. */
    public static final String[] RCS_ID = {
        "$URL$",
        "$Id$",
    };

	String appServer;
	String httpServer;
	String appName;
	int sipListenPort;
	String sipListenAddress;
	String outputDir;
	Logger logger;
	int remoteListenPort;
	
	public ConferenceSampleMachineTest() throws Exception {
		logger = this.getLogger();
		Properties props = new Properties();
		try {
			// Using getResourceAsStream(...) will read the properties file
			// copied from src/test/resources
			//
			// props.load(new FileInputStream("test.properties"));
			//
			File propertiesFile = new File("test.properties");
			if (propertiesFile.exists()) {
				props.load(new FileInputStream(propertiesFile));
			}
			else {
				props.load(
					ConferenceSampleMachineTest.class.getResourceAsStream(
					"/test.properties"));
			}

			// Allow properties to be overriden by system properties. This
			// is primarily to simplify configuration from a maven pom.xml
			// file.
			props.putAll(System.getProperties());

			appServer           = props.getProperty("SipAS");
			httpServer          = props.getProperty("HttpAS");
			sipListenPort       = Integer.parseInt(props.getProperty("SipStackListenPort"));
			sipListenAddress    = props.getProperty("SipStackListenIP", InetAddress.getLocalHost().getHostAddress());
			outputDir           = props.getProperty("OutputDir", "out");
			appName             = props.getProperty("AppName", "ConferenceSampleTest");

			init("ConferenceSampleTest");
		}
		catch (Exception e) {
			logger.error("error loading/reading test configuration file", e);
			throw e;
		}
	}

	private void init(String testName) throws CATException {
		CATConfig config = new CATConfig();
		config.setListenIP(this.sipListenAddress);
		config.setListenPort(this.sipListenPort);
		config.setTestName(testName);
		config.setOutputDir(outputDir);
		this.init(config);
	}

	@BeforeClass static public void runOnceBeforeAllTests() {		
	}

	@AfterClass static public void runOnceAfterAllTests() {
	}

	@Before public void runBeforeEachTest() {
		try {
			logger.info("running test setup");
		}
		catch (Exception e) {
			logger.error("test setup failed", e);
		}
	}

	@After public void runAfterEachTest() {
		try {
			logger.info("running test cleanup");
			this.release();
		}
		catch (Exception e) {
			logger.error("test cleanup failed", e);
		}
		logger.info("====================");
	}

	/** Test of a completed call from caller to callee.  
	 *  Caller ends call after callee answers.  RTP is
	 *  not tested.
	 * 
	 * @throws Throwable
	 */
	@Test public void testCompletedCall() throws Throwable {
		try {
			this.init("testCompletedCall");

			
			
			SIPAgent alice = createAgent("alice");
			SIPAgent bob = createAgent("bob");
			
			
			alice.setProxy(appServer);
			bob.setProxy(appServer);
			alice.call("sip:conf@10.10.5.32:5060");			
			pause(2000);
			bob.call("sip:conf@10.10.5.32:5060");
			
			

//			assertThat(alice, recvdNewSDP())); 
			//assertThat(callee, has(recvdRequest("INVITE")));


			
			/*pause(2000);
			assertThat(alice, is(connected()));

			pause(2000);*/
			
			
			
			
			pause(20000);
			
	//		assertThat(bob, recvdNewSDP()));
			assertThat(bob, is(connected()));
			pause(2000);
			
			//alice.end();
			

			pause(2000);
		/*	assertThat(alice, is(disconnected()));*/

			//bob.end();
			pause(2000);
			/*assertThat(bob, is(disconnected()));*/
 			
		}
		catch (Throwable e) {
			logger.error("test failed", e);
			throw e;
		}
	}
}
