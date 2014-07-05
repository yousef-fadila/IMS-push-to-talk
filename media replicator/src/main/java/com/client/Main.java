package com.client;

/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 */


import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.Charset;
import java.util.concurrent.ConcurrentHashMap;

import org.apache.mina.core.filterchain.DefaultIoFilterChainBuilder;
import org.apache.mina.filter.codec.ProtocolCodecFilter;
import org.apache.mina.filter.codec.textline.TextLineCodecFactory;
import org.apache.mina.filter.logging.LoggingFilter;
import org.apache.mina.transport.socket.DatagramSessionConfig;
import org.apache.mina.transport.socket.nio.NioDatagramAcceptor;
import org.apache.mina.transport.socket.nio.NioSocketAcceptor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.filter.RawFilter;
import com.handler.ConfigHandler;
import com.handler.PacketReplicatorHandler;


/**
 * The class that will accept and process clients in order to properly
 * track the memory usage.
 *
 * @author <a href="http://mina.apache.org">Apache MINA Project</a>
 */
public class Main {

    private static final long serialVersionUID = 1L;
    Logger logger = LoggerFactory.getLogger(Main.class);
    public static final int RTP_PORT = 50000;
    public static final int CONF_PORT = 50001;
    private ConcurrentHashMap<String, String> map = new ConcurrentHashMap<String, String>();
    private PacketReplicatorHandler handler = new PacketReplicatorHandler();

    public Main() throws IOException {
    	ConfigHandler configHandler = startRtpPort();
        startConfPort(configHandler);
        logger.debug("sssss");
        System.out.println("UDPServer listening on port for rtp " + RTP_PORT);
        System.out.println("UDPServer listening on port for conf " + CONF_PORT);
    }
    
    private ConfigHandler startRtpPort() throws IOException{
    	NioDatagramAcceptor acceptor = new NioDatagramAcceptor();
		acceptor.setHandler(handler);
        DefaultIoFilterChainBuilder chain = acceptor.getFilterChain();
        ConfigHandler configHandler = new ConfigHandler(handler);
        chain.addLast("raw", new RawFilter(configHandler));
        chain.addLast("logger", new LoggingFilter());

        DatagramSessionConfig dcfg = acceptor.getSessionConfig();
        dcfg.setReuseAddress(true);

        acceptor.bind(new InetSocketAddress(RTP_PORT));
        return configHandler;
    }
    
    
    private void startConfPort(ConfigHandler configHandler) throws IOException{
    	NioSocketAcceptor configAcceptor = new NioSocketAcceptor();
        configAcceptor.getFilterChain().addLast( "codec", new ProtocolCodecFilter( new TextLineCodecFactory( Charset.forName( "UTF-8" )))); 
        
		configAcceptor.setHandler(configHandler);
        configAcceptor.bind(new InetSocketAddress(CONF_PORT));
    }


    public static void main(String[] args) throws IOException {
        new Main();
    }
} 