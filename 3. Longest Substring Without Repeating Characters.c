int lengthOfLongestSubstring(char* s) {
    
    bool letterHash[127];
    memset(letterHash,false,sizeof(letterHash));
    
    int len = strlen(s);
    int charAscii;
    int curSubLen = 0;
    int longSubLen =  0;
    int startInd = 0;
    
    if(s == " ") return 0;
    
    int i;
    for(i=0;i<len;i++)
    {
        charAscii = s[i];
        if(letterHash[charAscii])
        {
            
            memset(letterHash,false,sizeof(letterHash));
            curSubLen = 0;
            startInd++;
            i = startInd;
        }
        charAscii = s[i];
        letterHash[charAscii] = true;
        curSubLen++;
        if(curSubLen > longSubLen) longSubLen = curSubLen;

    }
    
    return longSubLen;
}