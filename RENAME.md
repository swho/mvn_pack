# Maven java 專案 dependencies 匯入/匯出 
透過 mvn 將 pom、jar 匯出到另外一台電腦後，用 mvn 安裝在 local repository
1. `copy mvn_pack_run.exe 到 pom.xml資料夾`
2. `執行匯出`
3. `將target\dependency拷貝到對方電腦`
4. `執行dependency中的 mvn_pack_run.exe (可能需要連網下載plugin)`
