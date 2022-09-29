###############################################################
#                                                             #
#               Script to retrieve SSID Password.             #
#                                                             #
#                                                             #
#              HUELLOU Alexis, TAILLANDER Aliaume             #
#                                                             #
###############################################################

$wifi=@()

#Show blocked network
$cmd0=netsh wlan show blockednetworks
#List of SSID
$cmd1=netsh wlan show profiles
ForEach($row1 in $cmd1)
{
    #SSID Recuperation
    If($row1 -match 'Profil Tous les utilisateurs[^:]+:.(.+)$')
    {
        $ssid=$Matches[1]
        $cmd2=netsh wlan show profiles $ssid key=clear
        ForEach($row2 in $cmd2)
        {
            #Password Recuperation
            If($row2 -match 'Contenu de la c[^:]+:.(.+)$')
            {
                $key=$Matches[1]
                #We stock the password in a tab
                $wifi+=[PSCustomObject]@{ssid=$ssid;key=$key}
            }
        }
    }
}
#Export the tab into CSV file
$wifi|Export-CSV -Path 'c:\wifi.csv' -NoTypeInformation
#Show Tab
$wifi|Sort -Property ssid|Out-GridView -Title 'Mot de passe des - SSID enregistré'