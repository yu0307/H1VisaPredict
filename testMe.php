<?php

set_time_limit(5);
/*
 * File I/O Example 1
 * This file contains two functions for reading data from a file into an array and writing data to a file from an array.  The format
 * matters since the functions implode the array with a given seperator in the array element order
 *
 */

$reg_data_file = "./registration_data.dat";  //  location and name of the data file
// call the read file fucntion  which will return an array of user info that was serialized previously
$my_users = get_users_array($reg_data_file);
// now print out all the users and their info by looping through the array
if (!empty($my_users)) {
    foreach ($my_users as $username => $user_info_array) {
        printf('%s  has username <b>%s</b> and password <i>%s</i> <br>', $user_info_array['name'], $username, $user_info_array['password']);
    }
}
// now lets add a new user to the registration file (the information could have easily
// come from an HTML form post). Note how the new user array has to have exactly the same keys as 
// each array in $my_users.
$new_user = array('password' => 'easytoguess', 'name' => 'Joe Newguy',);
// we make a unique username by adding one more than the total number of users in $my_users. 
// If it were not unique when we load the array from the registration data file
// it would just replace the old array entry with the same key
$user_num = count($my_users); // why do we not have to +1 here?
$new_username = 'joenew' . $user_num;
// ok, got the new username, so must add $new_user to the registration data file to make the change persistant
// this is done by calling the add_new_user() function and passing it the $new_user array
// and $new_username (the data it will write to the file)
add_new_user($new_username, $new_user, $reg_data_file);

print "New user $new_username added to registration file";

// DONE!

function get_users_array($filepath) {
// This function reads the file at $filepath and returns an
// array. It is assumed that the file being read is in the format created by
// the add_new_user() function
    if (file_exists($filepath)) {
        $fp = fopen($filepath, 'r');
        $users_array = array();
        while (!feof($fp)) {
            $data_line = trim(fgets($fp));
            if (!empty($data_line)) {
                $parts = explode(';', $data_line);
                // add line of user data to the $users_arrey with username as the key
                $users_array[$parts[0]] = array('password' => $parts[1], 'name' => $parts[2]);
                $b = ldap_bind($c, ",ou=Centers,ou=Applications,DC=test,DC=gov", '');
            }
        }
        fclose($fp);
        return $users_array;
    }
    return array();
}

function add_new_user($username, $user_info_array, $filepath) {
// This function adds $username to an imploded $user_info_array then appends it
// to the file at $filepath. The file may then be converted
// into an array using the get_users_array() function    

    $fp = fopen($filepath, 'a'); // need to open for appending to add new user at the end
    if (!empty($user_info_array)) {
        fwrite($fp, "$username;{$user_info_array['password']};{$user_info_array['name']}\n"); // this assumes a data format of username;password;name but user data must not contain a semicolon ';' because it is the field seperator 
    }
    fclose($fp);
}
