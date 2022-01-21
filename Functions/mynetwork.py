import psutil



class NETWORKS():
    #Network Information
    def networks(self):
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()

            rowPosition = self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].isup), "net_stats_table")
            self.create_table_widget(rowPosition, 2, str(z[x].duplex), "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].speed), "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].mtu), "net_stats_table")

        #NET IO Counters
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)

            rowPosition = self.ui.net_io_table.rowCount()
            self.ui.net_io_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_io_table")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_sent), "net_io_table")
            self.create_table_widget(rowPosition, 2, str(z[x].bytes_recv), "net_io_table")
            self.create_table_widget(rowPosition, 3, str(z[x].packets_sent), "net_io_table")
            self.create_table_widget(rowPosition, 4, str(z[x].packets_recv), "net_io_table")
            self.create_table_widget(rowPosition, 5, str(z[x].errin), "net_io_table")
            self.create_table_widget(rowPosition, 6, str(z[x].errout), "net_io_table")
            self.create_table_widget(rowPosition, 7, str(z[x].dropin), "net_io_table")
            self.create_table_widget(rowPosition, 8, str(z[x].dropout), "net_io_table")

        #Net Addresses
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()

            for y in z[x]:
                rowPosition = self.ui.net_addresses_table.rowCount()
                self.ui.net_addresses_table.insertRow(rowPosition)

                self.create_table_widget(rowPosition, 0, str(x), "net_addresses_table")
                self.create_table_widget(rowPosition, 1, str(y.family), "net_addresses_table")
                self.create_table_widget(rowPosition, 2, str(y.address), "net_addresses_table")
                self.create_table_widget(rowPosition, 3, str(y.netmask), "net_addresses_table")
                self.create_table_widget(rowPosition, 4, str(y.broadcast), "net_addresses_table")
                self.create_table_widget(rowPosition, 5, str(y.ptp), "net_addresses_table")
        
        #Net Connections
        for x in psutil.net_connections():
            z = psutil.net_connections()

            rowPosition = self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)


            self.create_table_widget(rowPosition, 0, str(x.fd), "net_connections_table")
            self.create_table_widget(rowPosition, 1, str(x.family), "net_connections_table")    
            self.create_table_widget(rowPosition, 2, str(x.type), "net_connections_table")
            self.create_table_widget(rowPosition, 3, str(x.laddr), "net_connections_table")
            self.create_table_widget(rowPosition, 4, str(x.raddr), "net_connections_table")
            self.create_table_widget(rowPosition, 5, str(x.status), "net_connections_table")
            self.create_table_widget(rowPosition, 6, str(x.pid), "net_connections_table")
            


            







