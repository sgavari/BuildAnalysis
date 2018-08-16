# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:09:28 2018

@author: Sgavari
"""

from tkinter import *
from tkinter import ttk, filedialog,messagebox, END
import os, shutil
from os import path
import pandas as pd
from bs4 import BeautifulSoup
import csv
from datetime import datetime,  time as datetime_time, timedelta
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import re
import random
import decimal


class BuildAnalytics:
    
    def __init__ (self, master):
        self.master = master
        self.create_user_interface()
        self.master.protocol("WM_DELETE_WINDOW", self.close_callback)
        
    def create_user_interface (self):
        self.master.title('Build Analytics')
        self.master.resizable(True, False)
        
        self.main_frame = ttk.Frame(self.master)
        self.main_frame.pack(padx = 10, pady = 10)


# copying build event html
        
        ttk.Label(self.main_frame, text = 'Copy File From Source to Destination :').grid(row = 0, column = 0, sticky = 'w')
        ttk.Button(self.main_frame, text = 'Copy',
                   command = self.copy_builds).grid(row = 0, column = 1, columnspan = 2)     
        
        
#directory for source folder 
        
        ttk.Label(self.main_frame, text = 'Source File Path').grid(row = 2, column = 0, sticky = 'w')
        self.src_scm_entry = ttk.Entry(self.main_frame, width = 54)
        self.src_scm_entry.grid(row = 2, column = 1, sticky = 'e')

        self.src_scm_entry.insert(0, '')      
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_src_scm_callback).grid(row = 2, column = 2, sticky = 'w')
        
#directory for targetfolder :
        
        ttk.Label(self.main_frame, text = 'Destination File Path').grid(row = 3, column = 0, sticky = 'w')
        self.dest_scm_entry = ttk.Entry(self.main_frame, width = 54)
        self.dest_scm_entry.grid(row = 3, column = 1, sticky = 'e')

        self.dest_scm_entry.insert(0, '')      
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_dest_scm_callback).grid(row = 3, column = 2, sticky = 'w')  
        
        
#  Src path for converting html to csv and xml
        
        ttk.Label(self.main_frame, text = 'Source Directory:').grid(row = 6, column = 0, sticky = 'w')
        self.src_entry = ttk.Entry(self.main_frame, width = 54)
        self.src_entry.grid(row = 6, column = 1, sticky = 'e')
        self.src_entry.insert(0, '')      
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_src_callback).grid(row = 6, column = 2, sticky = 'w')

#  Destination path after converting html to csv and xml       
        ttk.Label(self.main_frame, text = 'Destination Directory:').grid(row = 7, column = 0, sticky = 'w')
        self.dest_entry = ttk.Entry(self.main_frame, width = 54)
        self.dest_entry.grid(row = 7, column = 1, sticky = 'e')
        self.dest_entry.insert(0, '')       
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_dest_callback).grid(row = 7, column = 2, sticky = 'w')
    
        
        self.convert_html_files = IntVar()
        self.convert_html_files.set(1)
        ttk.Checkbutton(self.main_frame, text = 'Convert Html File to CSV and XML format',
                        variable = self.convert_html_files).grid(row = 8, column = 0, columnspan = 1, sticky = 'w')
        
        
        self.copy_files = IntVar()
        self.copy_files.set(0)
        ttk.Checkbutton(self.main_frame, text = 'Copy Selected Files ',
        variable = self.copy_files).grid(row = 5, column = 0, columnspan = 1, sticky = 'w')

        
        ttk.Button(self.main_frame, text = 'Convert Data',
                   command = self.get_data_callback).grid(row = 5, column = 1, columnspan = 2)  
       
         
# Compare Two XMl File
         
        ttk.Label(self.main_frame, text = 'Compare Two  Xml Build files :').grid(row =9, column = 0, sticky = 'w')
        ttk.Button(self.main_frame, text = 'Compare Files',
                   command = self.compare_callback).grid(row = 9, column =1, columnspan = 2) 
        
#First file path for cmp
        ttk.Label(self.main_frame, text = 'First File').grid(row = 10, column = 0, sticky = 'w')
        self.src_cmp_entry = ttk.Entry(self.main_frame, width = 54)
        self.src_cmp_entry.grid(row = 10, column = 1, sticky = 'e')
        self.src_cmp_entry.insert(0, '\\Users\sthang\output')       
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_cmp_src_callback).grid(row = 10, column = 2, sticky = 'w')
        
        
#second file path for cmp
        
        ttk.Label(self.main_frame, text = 'Second File').grid(row = 11, column = 0, sticky = 'w')
        self.dest_cmp_entry = ttk.Entry(self.main_frame, width = 54)
        self.dest_cmp_entry.grid(row = 11, column = 1, sticky = 'e')
        self.dest_cmp_entry.insert(0, '\\Users\sthang\output')       
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_cmp_dest_callback).grid(row = 11, column = 2, sticky = 'w')
  
        
#src network callback  :
    def browse_src_scm_callback(self):
   
        filepath_scm = filedialog.askdirectory(initialdir = self.src_scm_entry.get())
    #        filepath = filedialog.askopenfilename(initialdir = self.src_entry.get(),filetypes = (("html files","*.html"),("all files","*.*")))
        self.src_scm_entry.delete(0, END)
        self.src_scm_entry.insert(0, filepath_scm)
        
        
#destination local callback:  
    def browse_dest_scm_callback(self):
        path_scm = filedialog.askdirectory(initialdir = self.dest_scm_entry.get())
        self.dest_scm_entry.delete(0, END)
        self.dest_scm_entry.insert(0, path_scm)  
                    
# Cmp src Callback        
    def browse_cmp_src_callback(self):    
        File1_filepath = filedialog.askopenfilename(initialdir = self.src_cmp_entry.get(),filetypes = (("Xml files","*.xml"),("all files","*.*")))
        self.src_cmp_entry.delete(0, END)
        self.src_cmp_entry.insert(0, File1_filepath)
        
# Cmp destination Callback      
    def browse_cmp_dest_callback(self):    
        File2_filepath = filedialog.askopenfilename(initialdir = self.dest_cmp_entry.get(),filetypes = (("Xml files","*.xml"),("all files","*.*")))
        self.dest_cmp_entry.delete(0, END)
        self.dest_cmp_entry.insert(0, File2_filepath)      
# Src Callback          
    def browse_src_callback(self):
        filepath = filedialog.askdirectory(initialdir = self.src_entry.get())
        self.src_entry.delete(0, END)
        self.src_entry.insert(0, filepath)
#Dest call back        
    def browse_dest_callback(self):
        path = filedialog.askdirectory(initialdir = self.dest_entry.get())
        self.dest_entry.delete(0, END)
        self.dest_entry.insert(0, path)  
        
#Plot bar chart     
    def plot_fig(self,xmlFile,filename,file_path): 
      
        tree = ET.parse(xmlFile)
        root = tree.getroot()
        listoftime=[]
        loads=[]
        diffs=[]
        randomcolor=decimal.Decimal(random.randrange(0, 100))/99
        listoftime_text =[]
        
        
        for row in root.findall('row'): 

            buildeventvalue = row.find('Build_Event').text
            if (buildeventvalue.find("Done creating the MDS databases")!=-1):
               
                date_time1 = row.find('Date_and_Time').text
                timetoloadmds =date_time1.split(' ', 1)[1]
                format_datetime1 = datetime.strptime(timetoloadmds, "%m/%d/%Y %H:%M:%S.%f")
            
            if buildeventvalue.find("Loading") !=-1:
              
               load =row.find('Build_Event').text
               date_time = row.find('Date_and_Time').text
               datetime_split=date_time.split(' ', 1)[1]
               listoftime_text.append(datetime_split)
               format_datetime = datetime.strptime(datetime_split, "%m/%d/%Y %H:%M:%S.%f")
               listoftime.append(format_datetime)
               loads.append(load)
               
           
        for i in range(len(listoftime)-1):
            timetocomplete = abs(listoftime[i+1] - listoftime[i])
            converttoseconds = timetocomplete.total_seconds()
            diffs.append(converttoseconds)
        ind=len(listoftime)-1 
        lastonbetocomplete = format_datetime1 -listoftime[ind]   
        diffs.append(lastonbetocomplete.total_seconds())  
        
        matches=[]
        for value in loads:    
            
            match=re.findall(r'\'(.+?)\'',value)
            mt=",".join(match)
            matches.append(mt)
         # Change of fontsize and angle of xticklabels   
        y_pos = np.arange(len(matches))
        plt.bar(y_pos, diffs, alpha=randomcolor)


        plt.xticks(y_pos, matches, fontsize=6,rotation=70)
        
        a =sum(i for i in diffs)
        min =a/60
        print("Total time taken in creating MDs data base: " , min)
        
        
        plt.ylabel('Time in Seconds')
        plt.title('MDS DataBase')
        
        plt.savefig(file_path+ "/" +filename + 'fig')
        plt.show()
        
#copy builds from network to local folder        
    def copy_builds(self) :
        file_path_scm =self.src_scm_entry.get()
        for dirName, subdirList, fileList in os.walk(file_path_scm):
            if "Dailys" and "Media" in subdirList:
              try:   
               subdirList.remove ("Dailys")
              except ValueError:
                  pass
              try:  
               subdirList.remove ("Media")
              except ValueError:
                  pass

            for fname in fileList:
                if fname =="BuildEventsLog.html":
                   normal_path=os.path.normpath(dirName)
                   src= os.path.join(normal_path,fname)
                   destin_path=self.dest_scm_entry.get()
                   print(destin_path)
                   print(normal_path)
                   folder_name= (os.path.split(os.path.split(normal_path)[1])[1])
                   print(folder_name)
#                   target_dir=os.path.normpath(os.path.join(destin_path,folder_name))
                   target_dir=os.path.normpath(os.path.join(destin_path))
                   print(destin_path)
                   print(target_dir)
                   if not os.path.exists(target_dir):
                      os.mkdir(target_dir)
                   
                   shutil.copy(src, target_dir)
                   rename_old_name=os.path.join(target_dir,fname)
                   rename_new_name=os.path.join(target_dir,os.path.split(os.path.split(dirName)[1])[1]+'.html')
                   print('old',rename_old_name)
                   print('new',rename_new_name)
                   os.rename(rename_old_name,rename_new_name)  
            
        print(file_path_scm)        
    
# CSV to XML coonverter    
    def Csv_Xml(self,filename,file_path,file_path2):   

        xmlFile = os.path.join(file_path+ "/" + filename + "." + 'xml')
        xmlData = open(xmlFile, 'w')
        xmlData.write('<?xml version="1.0"?>' + "\n")
        # there must be only one top-level tag
        xmlData.write('<BuildEvent>' + "\n")
        
        wakewordToCheck = ['targets','RoadRunner-BLIF','Cougar','MainUI','Win','MDS','JavaDoc','RoadRunner-BLIMP','Auxiliary','DesignServer','Mercury','x86','RTAP','Error']

        listoftime=[]
        listofdb=[]
        listtimetocomplete=[]
        listoftime_text=[]
        
        def start_date(i):
             date_time1=row[i]
             mdsloadtime =date_time1.split(' ', 1)[1]
             startdate=datetime.strptime(mdsloadtime, "%m/%d/%Y %H:%M:%S.%f")
                     
             xmlData.write('    ' + '<StartDate >'+ str(startdate) + '</StartDate >' + "\n")
             return startdate
        def end_date(i,x):
            date_time1=row[i]
            mdsloadtime =date_time1.split(' ', 1)[1]
            
            endate =datetime.strptime(mdsloadtime, "%m/%d/%Y %H:%M:%S.%f")
            v= endate-x
            xmlData.write('    ' + '<EndDate >' \
                  + str(endate) + '</EndDate >' + "\n")
            
            xmlData.write('    ' + '<Duration>' \
                 + str(v) + '</Duration>' + "\n")  
        def duration(timeduration):
             
             
             xmlData.write('    ' + '<Duration>' \
                 + str(timeduration) + '</Duration>' + "\n")  
        def time_format(date_time):
            datetime_split=date_time.split(' ', 1)[1]
            listoftime_text.append(datetime_split)
            datetime_format = datetime.strptime(datetime_split, "%m/%d/%Y %H:%M:%S.%f")
            return datetime_format
        for wakeword in wakewordToCheck:
         
               
           csvData = csv.reader(open(file_path2,'r'))
           for row  in csvData:
              

               if wakeword  in row[1] and ('Building' in row[1] or 'Generating' in row[1] or 'Copying' in row[1]):
                  xmlData.write('<'+ wakeword +'>' + "\n") 
                  x=start_date(0)
               
                  
               if wakeword in row[1] and 'Creating' in row[1] and 'database'  in row[1] :
                  xmlData.write('<'+ wakeword +'>' + "\n")
                  x=start_date(0)
                  csvData2 = csv.reader(open(file_path2,'r'))
                  for row  in csvData2:
                   if 'Loading' in row[1]:
                      match=re.findall(r'\'(.+?)\'',row[1])
                      mt=",".join(match)
                      listoftime.append(time_format(row[0]))
                      listofdb.append(mt)
                   elif 'Done' in row[1] and wakeword  in row[1]:
                      listoftime.append(time_format(row[0]))
                  for i in range(len(listoftime)-1):
                       timetocomplete = abs(listoftime[i+1] - listoftime[i])
                       listtimetocomplete.append(timetocomplete)
                  for i in range(len(listofdb)):
                           xmlData.write('<MDS'+ listofdb[i]+'>' +   "\n")
                           xmlData.write('<StartDate'+'>'+ str(listoftime[i]))
                           xmlData.write('</StartDate'+'>' + "\n") 
                           
                           xmlData.write('<Duration'+'>'+ str(listtimetocomplete[i])) 
                           xmlData.write('</Duration'+'>'+ "\n")    
                           
                           xmlData.write('</MDS'+ listofdb[i]+ '>' + "\n")
                   
                        
               elif 'Done' in row[1] and wakeword  in row[1] :
                     
                     end_date(0,x)
                     xmlData.write('</' + wakeword+ '>' + "\n")
                
        xmlData.write(xmlFile+'</BuildEvent>' + "\n")
        xmlData.close() 
  


 # copy and convert html file to csv      
    def get_data_callback(self):
        sourcepath= self.src_entry.get()
        source = os.listdir(sourcepath)
        destfilepath = self.dest_entry.get()
       
        if self.copy_files.get():
           for files in source:
               full_file_name = os.path.join(sourcepath, files)
               if (os.path.isfile(full_file_name)):
                  shutil.copy(full_file_name,destfilepath) 
                  
        if self.convert_html_files.get(): 
           for files in source:
               full_file_name = os.path.join(destfilepath, files)
               if (os.path.isfile(full_file_name)):
                    head,tail=path.split(full_file_name)
                    filename=os.path.splitext(tail)[0]
                    convertedfile = os.path.join(filename+ "." + 'csv')           
                    file=open(full_file_name,'r') 
                    soup = BeautifulSoup(file, 'lxml') # Parse the HTML as a string
                    table = soup.find_all('table')[0] # Grab the first table
#                    row_marker = 0
                    list_of_rows=[]
                    for row in table.find_all('tr'):
                            column_marker = 0
                            columns = row.find_all('td')
                            list_of_cells=[]
                            for column in columns:
                                 list_of_cells.append(column.text)
                                 column_marker+=1
                            list_of_rows.append(list_of_cells)
                    my_df = pd.DataFrame(list_of_rows)
                    file_path= destfilepath+"/" + filename
                    file_path2 =file_path+"/"+convertedfile
          
                    if not os.path.exists(file_path):
                     
                        os.makedirs(file_path)
                    if not os.path.exists(file_path2):
                        my_df.to_csv(file_path+"/"+convertedfile,index=False,header=False)
                        print( "\n"+ "Convertion of " + tail +" "+ "to"+ "  " + convertedfile +" is Completed." )
                    else:
                        print("\n" +  tail +" already exists in directory " + head )
                        
                    self.Csv_Xml(filename,file_path,file_path2)
                    
 #  Compare Two Files
    def  compare_callback(self):    
         
         
        xmlFile = self.src_cmp_entry.get()
        file_path = self.dest_cmp_entry.get()
        tree = ET.parse(xmlFile)
        
        src_build_name = os.path.split(os.path.split(xmlFile)[0])[1]
        trgt_build_name = os.path.split(os.path.split(file_path)[0])[1]
        
        tree1 = ET.parse(file_path)
        
        root = tree.getroot()
        root1 = tree1.getroot()
        listoftime=[]
        listoftime1=[]
        listoftime1_Pie=[]
        listoftime_Pie=[]
        matches=[]
        matches1=[]
        mdsbuilds=[]
        mdsbuildsduration=[] 
        mdsbuilds1=[]
        mdsbuildsduration1=[] 
        mdsbuildsduration1_pie=[]
        mdsbuildsduration_pie=[]
        for row in root:
           if(row.tag == 'targets'):
               timefortarget1= row.find("Duration").text
               buildStrtdate=datetime.strptime(row.find("StartDate").text,'%Y-%m-%d %H:%M:%S.%f').date()

               try:
                 total_datetime1 = datetime.strptime(timefortarget1, "%H:%M:%S.%f").time()
                 print(total_datetime1)
               except ValueError:
                 total_datetime1 = datetime.strptime(timefortarget1, "%H:%M:%S").time()
                 print(total_datetime1)

           else:
               if(row.tag=='MDS'):
                  for c in row:            
                       t =c.find("Duration")
                       if(t!=None):
                         mdsbuilds1.append(c.tag)
                         try:
                           mds_format_datetime1 = datetime.strptime(t.text, "%H:%M:%S.%f")
                         except ValueError:
                           mds_format_datetime1 = datetime.strptime(t.text, "%H:%M:%S")
                         mdsbuildsduration1_pie.append(mds_format_datetime1.minute+ mds_format_datetime1.second/60 + mds_format_datetime1.hour*60 )
                         mdsbuildsduration1.append(mds_format_datetime1.time())
               matches.append(row.tag)   
               t =row.find("Duration").text
               try:
                format_datetime1 = datetime.strptime(t, "%H:%M:%S.%f")
               except ValueError:
                format_datetime1 = datetime.strptime(t, "%H:%M:%S")
               listoftime_Pie.append(format_datetime1.minute+ format_datetime1.second/60 + format_datetime1.hour*60 )
               listoftime.append(format_datetime1.time())

        kv1 =dict(zip(mdsbuilds1, mdsbuildsduration1))     
        
        kv3=dict(zip(matches,listoftime))
        kv1.update(kv3)   
        
        mdslistforjs1 ='[{}]'.format(' '.join("['{}',{}],".format(k, v) for k, v in zip(mdsbuilds1, mdsbuildsduration1_pie)))
        targetlistforjs1='[{}]'.format(' '.join("['{}',{}],".format(k, v) for k, v in zip(matches, listoftime_Pie)))
        for row in root1:
           if(row.tag == 'targets'):
               timefortarget2= row.find("Duration").text
               buildStrtdate2=datetime.strptime(row.find("StartDate").text,'%Y-%m-%d %H:%M:%S.%f').date()
                   
               try:
                  total_datetime2 = datetime.strptime(timefortarget2, "%H:%M:%S.%f").time()
               except ValueError:
                  total_datetime2 = datetime.strptime(timefortarget2, "%H:%M:%S").time()     
               
           else:
               if(row.tag=='MDS'):
                  for c in row:
                       
                       t =c.find("Duration")
                       if(t!=None):
                         mdsbuilds.append(c.tag)
        #                 mdsbuildsduration.append(t.text)
                         
                         try:
                           mds_format_datetime2 = datetime.strptime(t.text, "%H:%M:%S.%f")   
                         except ValueError:
                           mds_format_datetime2 = datetime.strptime(t.text, "%H:%M:%S")
              
                         mdsbuildsduration_pie.append(mds_format_datetime2.minute+ mds_format_datetime2.second/60 + mds_format_datetime2.hour*60 )    
                         mdsbuildsduration.append(mds_format_datetime2.time())   
               matches1.append(row.tag)             
               t =row.find("Duration").text
               
               try:
                format_datetime2 = datetime.strptime(t, "%H:%M:%S.%f")   
               except ValueError:
                format_datetime2 = datetime.strptime(t, "%H:%M:%S")
               
               listoftime1_Pie.append(format_datetime2.minute+ format_datetime2.second/60 + format_datetime2.hour*60 )  
               listoftime1.append(format_datetime2.time())
        kv2 =dict(zip(mdsbuilds, mdsbuildsduration))       
        kv4= dict(zip(matches1, listoftime1))  
        mdslistforjs ='[{}]'.format(' '.join("['{}',{}],".format(k, v) for k, v in zip(mdsbuilds, mdsbuildsduration_pie)))
        targetlistforjs='[{}]'.format(' '.join("['{}',{}],".format(k, v) for k, v in zip(matches1, listoftime1_Pie)))

        kv2.update(kv4)       
        Build_name_date1 = 'Build Name :'+ src_build_name +' and Build Date:' + str(buildStrtdate)
       
        Build_name_date2 = 'Build Name :' + trgt_build_name + ' and  Build Date:'+ str(buildStrtdate2)

        df1 = pd.DataFrame({ Build_name_date1 : kv1})
        
        df2 = pd.DataFrame({Build_name_date2 : kv2})

        df3 = pd.concat([df1, df2],axis=1) 
        df3.columns.name = 'Targets'
        
        
        df4 = pd.DataFrame([[ total_datetime1, total_datetime2]],columns=[Build_name_date1, Build_name_date2])
        df5=df4.rename(index={0: ' Total Targets Build time'})
        result =df3.append(df5)
        
        result.to_html('Build_Analytics.html')
        with open('Build_Analytics.html', 'a') as file:
            
            Java_Script1="""<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js">
                          </script>
                          <script type="text/javascript">
                    
                          // Load Charts and the corechart package.
                          google.charts.load('current', {'packages':['corechart']});
                    
                          // Draw the pie chart for First file when Charts is loaded.
                          google.charts.setOnLoadCallback(drawFirstChart);
                    
                          // Draw the pie chart for the Second file when Charts is loaded.
                          google.charts.setOnLoadCallback(drawSecondChart);
                    
                         // Callback that draws the pie chart for Sarah's pizza.
                          
                          function drawFirstChart() {
                    
                            // Create the data table .
                            var data = new google.visualization.DataTable();
                            data.addColumn('string', 'Topping');
                            data.addColumn('number', 'Slices');"""
            Java_Script3=""" 
                           var options = {{{value},width:700,height:600}};""".format(value ="title:"+ "'Log Event for Build"+str(src_build_name)+"'")
                    
            Java_Script13=             """   // Instantiate and draw the chart for first file.
                            var chart = new google.visualization.PieChart(document.getElementById('First_File'));
                            function selectHandler() {
									  var selectedItem = chart.getSelection()[0];
									  
									  if (selectedItem ) {
										 var topping = data.getValue(selectedItem.row, 0);
										 if(topping=='MDS'){
											 alert('The user selected ' + topping);
											 var data3 = new google.visualization.DataTable();
												data3.addColumn('string', 'Topping');
												data3.addColumn('number', 'Slices');"""

											
			 
            Java_Script2=""" data.addRows({length})""".format(length=targetlistforjs1)  
           
            Java_Script4=""" data3.addRows({length1})""".format(length1=mdslistforjs1) 
            
            Java_Script7=""" data_Second.addRows({length_target})""".format(length_target=targetlistforjs) 
            Java_Script9=""" data4.addRows({length_MDS})""".format(length_MDS=mdslistforjs) 
            Java_Script5=""" 						
                                       var options3 = {{{value1},'width':700,'height':600}};""".format(value1="'title':""'MDS Log for Build"+str(src_build_name)+"'")
															   
            Java_Script5_14=""" var chart3 = new google.visualization.PieChart(document.getElementById('First_File_2'));
											 google.visualization.events.addListener(chart3, 'select', selectHandler);    
											 chart3.draw(data3, options3)
											 }
										 
									  }
									}
                            google.visualization.events.addListener(chart, 'select', selectHandler);   
                            chart.draw(data, options);
                          }"""
                    
            Java_Script6="""             // Callback that draws the pie chart for Anthony's pizza.
                          function drawSecondChart() {
                    
                            // Create the data table for Anthony's pizza.
                            var data_Second = new google.visualization.DataTable();
                            data_Second.addColumn('string', 'Topping');
                            data_Second.addColumn('number', 'Slices');
                            """
                    
            Java_Script8="""      // Set options for Anthony's pie chart.
                            var options = {{{value2},width:700,height:600}}; """.format(value2="'title':""'Log Event for Build"+str(trgt_build_name)+"'")
													                                   
            Java_Script8_15= """   // Instantiate and draw the chart for Sarah's pizza.
                            var chart_Second = new google.visualization.PieChart(document.getElementById('Second_File'));
                            function selectHandler() {
									  var selectedItem = chart_Second.getSelection()[0];
									  
									  if (selectedItem ) {
										 var topping = data_Second.getValue(selectedItem.row, 0);
										 if(topping=='MDS'){
											 alert('The user selected ' + topping);
											 var data4 = new google.visualization.DataTable();
												data4.addColumn('string', 'Topping');
												data4.addColumn('number', 'Slices');"""

            Java_Script10="""
                                    var options4 = {{{value3},'width':700,'height':600}};""".format(value3="'title':""'MDS Log for Build"+str(trgt_build_name)+"'")
															
            Java_Script10_16= """
                                var chart4 = new google.visualization.PieChart(document.getElementById('Second_File_2'));
											 google.visualization.events.addListener(chart4, 'select', selectHandler);  
                                        chart4.draw(data4, options4)
											 }
										}
							 }      
                            // Instantiate and draw the chart for Second File.
                         
                            google.visualization.events.addListener(chart_Second, 'select', selectHandler);   
                            chart_Second.draw(data_Second, options);
                          }
                        </script>
                      </head>
                    
                        <!--Table and divs that hold the pie charts-->
                        <table class="columns">
                          <tr>
                            <td><div id="First_File" style="border: 1px solid #ccc"></div></td>
                            <td><div id="Second_File" style="border: 1px solid #ccc"></div></td>
                          </tr>
                        </table>
                         <table class="rows">
                          <tr>
                             <td><div id="First_File_2" style="border: 1px solid #ccc"></div></td>
                             <td><div id="Second_File_2" style="border: 1px solid #ccc"></div></td>
                         </tr>
                        </table>"""
            Java_Script=Java_Script1+Java_Script2+Java_Script3+Java_Script13+Java_Script4+Java_Script5+Java_Script5_14+Java_Script6+Java_Script7+Java_Script8+Java_Script8_15+Java_Script9+Java_Script10+Java_Script10_16
            file.write(Java_Script)
        file.close
        
    def  close_callback(self):
         self.master.destroy() # perform other cleanup
           
         
def main():
    root = Tk() # get window
    gui = BuildAnalytics(root)
    root.mainloop() # Tk event loop
    

if __name__ == "__main__": main()  