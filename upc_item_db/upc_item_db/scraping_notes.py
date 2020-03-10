# Xpath cheatsheet: https://devhints.io/xpath
# https://stackoverflow.com/questions/21455349/xpath-query-get-attribute-href-from-a-tag



# normal table
table = response.xpath('//*[@class="detail-list"]')
rows = table.xpath('//tr')
row = rows[2]
row.xpath('td//text()')[0].extract()
rows[0].xpath('td//text()')[1].extract()

#tabe with href links
aa = table.xpath('//a')
aa = table.xpath('.//a') <-- Do is important to make it relative to table

aa = table.xpath('.//a/@href').extract()
aa = aa.css('::text').extract()

ab = table.xpath('.//a')


-----------Proxy vs User_Agent
# Already rotates User Agents: https://support.scrapinghub.com/support/solutions/articles/22000188404-customizing-crawlera-user-agents

https://github.com/hyan15/scrapy-proxy-pool
https://pypi.org/project/scrapy-user-agents/

Google Search: "proxy vs user agent scrapy"

https://www.youtube.com/watch?v=090tLVr0l7s&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=24

May be able to just use
Googlebot/2.1 (+http://www.google.com/bot.html)


--TOR
# https://pkmishra.github.io/blog/2013/03/18/how-to-run-scrapy-with-TOR-and-multiple-browser-agents-part-1-mac/
# https://www.torproject.org/docs/documentation.html.en

SOCKS proxy?

# gives good TOR outline with scrapy
http://akul.me/blog/2017/proxy-cheatsheet/

# read about:
# Privoxy - https://www.privoxy.org/
# socket proxy ("good") vs http proxy ("bad")

https://blog.michaelyin.info/scrapy-socket-proxy/

tor is a SOCKS proxy, while privoxy and polipo are HTTP proxies.

# https://en.wikipedia.org/wiki/Tor_(anonymity_network)

# Top 1000 Websites Blocking VPN & TOR Users
https://jerrygamblin.com/2016/07/06/top-1000-websites-blocking-vpn-tor-users/

# Python Network Programming - TCP/IP Socket Programming
# https://www.google.com/search?biw=1148&bih=1098&ei=HFz1XLCSCY-2swXn2LmYAw&q=Python+Network+Programming+-+TCP%2FIP+Socket+Programming&oq=Python+Network+Programming+-+TCP%2FIP+Socket+Programming&gs_l=psy-ab.3..0j0i22i30.25871.25871..26318...0.0..0.106.106.0j1......0....2j1..gws-wiz.......0i71.rsD8amniEGY
https://realpython.com/python-sockets/ --> On "Handling Multiple Connections"
# inter-process communication (IPC)
# Transmission Control Protocol (TCP) --> "good"
# User Datagram Protocol (UDP) --> "bad"
# port should be an integer from 1-65535 (0 is reserved). It’s the TCP port number to accept connections on from clients. Some systems may require superuser privileges if the port is < 1024.


------Create own Proxy server
# https://www.geeksforgeeks.org/creating-a-proxy-webserver-in-python-set-1/


--Scrapy Splash and all Scrapy Open Soruce things :
 https://scrapinghub.com/open-source
# https://github.com/scrapy-plugins/scrapy-splash


MechanicalSoup
# https://github.com/MechanicalSoup/MechanicalSoup
# https://mechanicalsoup.readthedocs.io/en/stable/mechanicalsoup.html
# has a place to put the User Agent

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},  # Use the lxml HTML parser
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)
