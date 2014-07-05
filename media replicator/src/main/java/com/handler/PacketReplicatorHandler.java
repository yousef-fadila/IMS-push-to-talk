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

import java.net.InetSocketAddress;
import java.util.concurrent.ConcurrentHashMap;

import org.apache.mina.core.IoUtil;
import org.apache.mina.core.future.ConnectFuture;
import org.apache.mina.core.future.IoFuture;
import org.apache.mina.core.future.IoFutureListener;
import org.apache.mina.core.service.IoConnector;
import org.apache.mina.core.service.IoHandlerAdapter;
import org.apache.mina.core.session.IdleStatus;
import org.apache.mina.core.session.IoSession;
import org.apache.mina.transport.socket.nio.NioDatagramConnector;

public class PacketReplicatorHandler extends IoHandlerAdapter {

	private IoConnector connector = new NioDatagramConnector();;
    private ConcurrentHashMap<String, IoSession> map = new ConcurrentHashMap<String, IoSession>();
    
    public PacketReplicatorHandler() {
    }
    
    public void createNewSession(final String ip, final int port){
    	NioDatagramConnector connector = new NioDatagramConnector();
    	 connector.setHandler(this);
    	 final ConnectFuture connFuture = connector.connect(new InetSocketAddress(
    			 ip, port));
    	 connFuture.addListener(new IoFutureListener<IoFuture>(){

			public void operationComplete(IoFuture future) {
				IoSession session2 = connFuture.getSession();
		    	 if(session2 !=null){
		    		 map.put(ip, session2);
		    	 }
			}
    		 
    	 });
    }
    
    public IoSession removeSession(String ip,boolean close){
    	IoSession remove = map.remove(ip);
    	if(close && remove != null){
    		remove.close(true);
    	} 
    	return remove;
    }
    
    public void addSession(String ip,IoSession session){
    	map.put(ip,session);    	
    }

    @Override
    public void exceptionCaught(IoSession session, Throwable cause)
            throws Exception {
        cause.printStackTrace();
        session.close(true);
    }

    @Override
    public void messageReceived(IoSession session, Object message)
            throws Exception {    	 
    	 IoUtil.broadcast(message, map.values());
    	
    }

    @Override
    public void sessionClosed(IoSession session) throws Exception {
        System.out.println("Session closed...");
    }

    @Override
    public void sessionCreated(IoSession session) throws Exception {

        System.out.println("Session created...");

    }

    @Override
    public void sessionIdle(IoSession session, IdleStatus status)
            throws Exception {
        System.out.println("Session idle...");
    }

    @Override
    public void sessionOpened(IoSession session) throws Exception {
        System.out.println("Session Opened...");
    }

}
