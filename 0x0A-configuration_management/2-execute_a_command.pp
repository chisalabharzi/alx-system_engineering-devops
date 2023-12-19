# manifest that kills a process named killmenow, with puppet

exec { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0, 1]
}
