/**************************************************************
 *      Template EChartsMachineToJava interface definition    *
 **************************************************************/

// $Name:  $ $Id: $

package att.com.ConferenceSample;

/** Interface defining methods called by the application to access the
 *  environment (e.g., get data from external resource, update environment
 *  with call-state data).
 */
public interface ConferenceSampleMachineToJava {
	
	void addUser(String confName, String username);
	void removeUser(String confName, String username);
	void pttON(String confName, String username);
	void pttOFF(String confName, String username);
}
