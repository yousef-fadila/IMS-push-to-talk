/*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
* THE SOFTWARE.
* 
*
* Author: Yousef Fadila 
* Date: April 2012
*
*/
 
package com.handler;

import java.util.concurrent.ConcurrentHashMap;

import org.apache.mina.core.service.IoHandler;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.core.session.IoSession;

public class ConfigHandler implements IoHandler {

	private PacketReplicatorHandler handler;
	private IoSession sessionTalk; 
	private ConcurrentHashMap<String, String> map = new ConcurrentHashMap<String, String>();
	private String ipTalker;
	public String getIpTalker() {
		return ipTalker;
	}

	private enum Header{
		ADD,REMOVE,PTTON,PTTOFF
	}
	public ConfigHandler() {
		// TODO Auto-generated constructor stub
	}
	
	public ConfigHandler(PacketReplicatorHandler handler) {
		this.handler = handler;
	}


	public void exceptionCaught(IoSession session, Throwable cause)
			throws Exception {
		// TODO Auto-generated method stub
		
	}

	public void messageReceived(IoSession session, Object message)
			throws Exception {
		String messageStr = message.toString();
		System.out.println(messageStr);
		String[] headerSplit = messageStr.split("@");
		String headerStr = headerSplit[0];
		Header header = Header.valueOf(headerStr);
		String[] split = headerSplit[1].split(":");
		
		String ip = split[0];
		String port = split[1];
		
		System.out.println("START - THE MAP " + map.toString());
		
		switch (header) {
		case ADD:
			
			map.put(ip, port);
			handler.createNewSession(ip, Integer.parseInt(port));
			break;
		case REMOVE:
			map.remove(ip);
			handler.removeSession(ip, true);
			break;
		case PTTON:
			map.remove(ip);
			sessionTalk = handler.removeSession(ip, false);
			ipTalker = ip;
			break;
		case PTTOFF:
			map.put(ip, port);
			handler.addSession(ip, sessionTalk);
			ipTalker = null;
			break;
		default:
			throw new IllegalArgumentException("header not supported on config port");
		}
		System.out.println("START - THE MAP " + map.toString());
		
	}

	public void messageSent(IoSession session, Object message)
			throws Exception {
		// TODO Auto-generated method stub
		
	}

	public void sessionClosed(IoSession session) throws Exception {
		// TODO Auto-generated method stub
		
	}

	public void sessionCreated(IoSession session) throws Exception {
		System.out.println("sessionCreated");
		
	}

	public void sessionIdle(IoSession session, IdleStatus status)
			throws Exception {
		// TODO Auto-generated method stub
		
	}

	public void sessionOpened(IoSession session) throws Exception {
		System.out.println("sessionOpened");
		
	}
	
}
