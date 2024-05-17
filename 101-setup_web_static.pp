#!/usr/bin/puppet

exec { '/usr/sbin/nginx':
  path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  user    => 'root',
  group   => 'root',
  creates => '/usr/sbin/nginx',
}

file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '755',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '755',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '755',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '755',
}

file { '/data/web_static/releases/test':
  ensure => 'link',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '755',
  target => '/data/web_static/current',
}
