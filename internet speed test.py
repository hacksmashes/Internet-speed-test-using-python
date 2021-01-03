import speedtest

ist=speedtest.Speedtest()
print("Download speed : ",ist.download())
print("Upload speed : ",ist.upload())



        # output will be in the form of bytes




        # 10 lakh bytes = 1Mbps


        
        # here the output is 90 lakh bytes, so our speed is 9Mbps (for downloading)




        # here the output is 20 lakh bytes, so our speed is 2Mbps (for uploading)




        # just ignore the values after the point ( . ) in the output



