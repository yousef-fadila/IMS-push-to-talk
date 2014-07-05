package messages;

import finals.MediaServerCommand;

public class OutLegMessage {

	private final String ip;
	private final int port;
	private final String username;
	private final MediaServerCommand msCommand;
	
	public OutLegMessage(String ip, int port, String username, MediaServerCommand msCommnad ) {
		super();
		this.ip = ip;
		this.port = port;
		this.msCommand = msCommnad;
		this.username = username;
	}

	public String getIp() {
		return ip;
	}

	public int getPort() {
		return port;
	}
	public String getUsername() {
		return username;
	}

	public MediaServerCommand getMsCommnad() {
		return msCommand;
	}
	
	public boolean isLegal() {
		return getMsCommnad().isLegal();
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((ip == null) ? 0 : ip.hashCode());
		result = prime * result
				+ ((msCommand == null) ? 0 : msCommand.hashCode());
		result = prime * result + port;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		OutLegMessage other = (OutLegMessage) obj;
		if (ip == null) {
			if (other.ip != null)
				return false;
		} else if (!ip.equals(other.ip))
			return false;
		if (msCommand != other.msCommand)
			return false;
		if (port != other.port)
			return false;
		return true;
	}

	
	@Override
	public String toString() {
		return "OutLegMessage [ip=" + ip + ", port=" + port + ", msCommnad="
				+ msCommand + "]";
	}
	
	public String generateCmd() {
		return msCommand.name() + MediaServerCommand.HEADER_SEPERATOR + ip + MediaServerCommand.IP_PORT_SEPERATOR + port;
	}
	
	public boolean isPTTONMessage() {
		return MediaServerCommand.PTTON == msCommand;
	}
	
	public boolean isPTTOFFMessage() {
		return MediaServerCommand.PTTOFF == msCommand;
	}
	public boolean isAddRemoveMessage() {
		return MediaServerCommand.ADD == msCommand || MediaServerCommand.REMOVE == msCommand;
	}

	public OutLegMessage cloneMsg(MediaServerCommand newCmd) {
		return new OutLegMessage(ip, port, username, newCmd);
	}
}
