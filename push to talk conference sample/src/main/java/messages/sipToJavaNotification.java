package messages;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import att.com.ConferenceSample.*;

public class sipToJavaNotification {
	final private String confName;
	ConferenceSampleMachineToJava toJave;
	
	public sipToJavaNotification(String confName,
			ConferenceSampleMachineToJava toJave) {
		super();
		this.confName = confName;
		this.toJave = toJave;
	}

	public void addUser(String username) {
		toJave.addUser(confName, username);
	}

	public void pttOFF(String username) {
		toJave.pttOFF(confName, username);
	}

	public void pttON(String username) {
		toJave.pttON(confName, username);
	}

	public void removeUser(String username) {
		toJave.removeUser(confName, username);
	}
}
