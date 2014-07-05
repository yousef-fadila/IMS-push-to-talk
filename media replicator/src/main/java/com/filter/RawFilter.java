package com.filter;
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
 
import java.net.InetSocketAddress;
import java.net.SocketAddress;

import org.apache.mina.core.filterchain.IoFilterAdapter;
import org.apache.mina.core.session.IoSession;

import com.handler.ConfigHandler;

public class RawFilter extends IoFilterAdapter {
	
	private ConfigHandler handler;
	public RawFilter(ConfigHandler handler) {
		this.handler = handler;
	}
	
	
	
	@Override
	public void messageReceived(NextFilter nextFilter, IoSession session,
			Object message) throws Exception {
		SocketAddress localAddress = session.getRemoteAddress();
    	String hostAddress = ((InetSocketAddress)localAddress).getAddress().getHostAddress();
//    	int port = ((InetSocketAddress)localAddress).getPort();
    	if(handler.getIpTalker() !=null && handler.getIpTalker().equals(hostAddress)){
    		super.messageReceived(nextFilter, session, message);
    	}
	}


}
