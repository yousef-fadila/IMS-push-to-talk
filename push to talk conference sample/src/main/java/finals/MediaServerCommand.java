package finals;

public enum MediaServerCommand {
	
	 
	
	ADD,REMOVE,PTTON,PTTOFF,ILLEGAL;
	
/*	private char dtmfMapping;
	
	private MediaServerCommand(char dtmfMapping) {
		this.dtmfMapping = dtmfMapping;
	}*/
	
	public boolean isLegal() {
		return this != ILLEGAL;		
	}
	
	public static final String HEADER_SEPERATOR = "@";
	public static final String IP_PORT_SEPERATOR = ":";
}
