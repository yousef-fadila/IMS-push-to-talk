/**************************************************************
 *           Template EChartsSipServlet subclass              *
 **************************************************************/

// $Name:  $ $Id: $

package att.com.ConferenceSample;

import java.util.Set;
import java.util.HashSet;
import javax.servlet.ServletConfig;
import javax.servlet.sip.*;
import javax.servlet.sip.SipServletRequest;


import org.echarts.servlet.sip.EChartsSipServlet;

/** Sample comment
 */
public class ConferenceSampleSipServlet extends EChartsSipServlet {
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public static final String rcsid = "$Id: $ $Name:  $";
    public final Set<String> set = new HashSet<String>();
    // Put one-time initialization code here.
    //
    @Override
    public void servletInit(ServletConfig sc) throws Exception {
    	
    }

    // Put one-time clean-up code here.
    //
    @Override
    public void destroy() {
    	for (String session: set)
    	{
    		SipApplicationSession sess = getApplicationSession(session);
    		if (sess != null) 
    			sess.invalidate();
    	}

    	set.clear();  
   
    	//getApplicationSession()
    }

    // Implement custom session key calculation if desired
    // (bound box only)
    //
    @Override
    protected String sessionKeyFromRequest(SipServletRequest req) {
    	System.out.println("Servlet sessionKetFromRquest "+ req);

        SipURI uri = ((SipURI)req.getTo().getURI());
        String sessionkey = uri.getUser();
        System.out.println(sessionkey);
        set.add(sessionkey);
        //the session key is the conference name      
        return sessionkey;
    }
}
