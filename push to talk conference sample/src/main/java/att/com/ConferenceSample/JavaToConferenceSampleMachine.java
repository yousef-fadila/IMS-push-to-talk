/**************************************************************
 *         Template JavaToEChartsMachine implementation       *
 **************************************************************/

// $Name:  $ $Id: $

package att.com.ConferenceSample;

import org.echarts.TransitionMachine;
import org.echarts.servlet.sip.JavaToEChartsMachine;

/** Mechanism for external environment to call methods on the application.
 *  May delegate commands to machine via ConferenceSampleMachineControl.
 */
public class JavaToConferenceSampleMachine extends JavaToEChartsMachine {

    /** Control interface for the machine.
     */
    ConferenceSampleControl control;

    // This method is called by the framework immediately after initialization
    //
    protected void init(TransitionMachine machine) throws Exception {
	    super.init(machine);
	    
	    control = (ConferenceSampleControl) machine;
    }

}
