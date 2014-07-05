/**************************************************************
 *         Template EChartsMachineToJava implementation       *
 **************************************************************/

// $Name:  $ $Id: $

package att.com.ConferenceSample;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import org.echarts.servlet.sip.EChartsMachineToJava;

import att.com.ConferenceSample.ConferenceSampleMachineToJava;

/** Sample implementation comment
 */
public class ConferenceSampleMachineToJavaImpl extends EChartsMachineToJava implements ConferenceSampleMachineToJava {
	private enum SQLAction {ADD,REMOVE,PTTON,PTTOFF};
		
	private void processSql(String tbl, String user, SQLAction action )
	{
		System.out.println("processSql, user " + user + " action " + action);
		
		Connection con = null;
		Statement stm = null;
		try {
		
		Context ctx = new InitialContext();
		DataSource ds = (DataSource) ctx.lookup("webConfDB_JNDI");
		con = ds.getConnection();
	    stm = con.createStatement();
        
         /* TODO create table of name "tbl" currently we put all users in one table for demo purposes. */
         
		String createTable = "CREATE TABLE conf(UserName varchar(50), PPT integer)";
		stm.executeUpdate(createTable);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
         
		String stmSql = "";
		switch (action)
		{
		case ADD:
			stmSql = "INSERT INTO conf VALUES ('" +   user + " ', 0)";
			break;
		case REMOVE:
			stmSql = "delete from conf where UserName = '" +  user + "'";
			break;
		case PTTON:
			stmSql = "UPDATE conf set PPT = 1 where UserName ='" + user + "'";
			break;
		case PTTOFF:
			stmSql = "UPDATE conf set PPT =0 where UserName ='" + user + "'";
			break;
		}
		
		try {
			if (!stmSql.equals(""))
				stm.executeUpdate(stmSql);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}        
   	}
	
	public void addUser(String confName, String username) {
		processSql(confName, username, SQLAction.ADD);
		
	}

	public void pttOFF(String confName, String username) {
		processSql(confName, username, SQLAction.PTTOFF);
		
	}

	public void pttON(String confName, String username) {
		processSql(confName, username, SQLAction.PTTON);
		
	}

	public void removeUser(String confName, String username) {
		processSql(confName, username, SQLAction.REMOVE);
		
	}
	
}
