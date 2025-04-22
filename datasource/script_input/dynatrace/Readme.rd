curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,defaultAggregation&metricSelector=builtin:host.cpu.*' \
-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
-H 'Accept: application/json'

#example data 
metricId,displayName,defaultAggregation
builtin:host.cpu.entc,AIX Entitlement used,avg
builtin:host.cpu.entConfig,AIX Entitlement configured,avg
builtin:host.cpu.idle,CPU idle,avg
builtin:host.cpu.iowait,CPU I/O wait,avg
builtin:host.cpu.load,System load,avg
builtin:host.cpu.load15m,System load15m,avg
builtin:host.cpu.load5m,System load5m,avg
builtin:host.cpu.msu.avg,MSU average,avg
builtin:host.cpu.msu.capacity,MSU capacity,avg
builtin:host.cpu.other,CPU other,avg
builtin:host.cpu.physc,AIX Physical consumed,avg
builtin:host.cpu.steal,CPU steal,avg
builtin:host.cpu.system,CPU system,avg
builtin:host.cpu.usage,CPU usage %,avg
builtin:host.cpu.user,CPU user,avg
builtin:host.cpu.ziip.eligible,zIIP eligible,avg
builtin:host.cpu.ziip.usage,zIIP usage,avg

#example data
{
  "totalCount": 3,
  "nextPageKey": null,
  "metrics": [
    {
      "metricId": "builtin:host.cpu.idle",
      "displayName": "CPU idle",
      "description": "",
      "unit": "Percent",
      "entityType": [
        "HOST"
      ],
      "aggregationTypes": [
        "auto",
        "avg",
        "max",
        "min"
      ],
      "transformations": [
        "filter",
        "fold",
        "merge",
        "names",
        "parents"
      ],
      "defaultAggregation": {
        "type": "avg"
      },
      "dimensionDefinitions": [
        {
          "key": "dt.entity.host",
          "name": "Host",
          "index": 0,
          "type": "ENTITY"
        }
      ]
    },
    {
      "metricId": "builtin:host.cpu.load",
      "displayName": "System load",
      "description": "",
      "unit": "Ratio",
      "entityType": [
        "HOST"
      ],
      "aggregationTypes": [
        "auto",
        "avg",
        "max",
        "min"
      ],
      "transformations": [
        "filter",
        "fold",
        "merge",
        "names",
        "parents"
      ],
      "defaultAggregation": {
        "type": "avg"
      },
      "dimensionDefinitions": [
        {
          "key": "dt.entity.host",
          "name": "Host",
          "index": 0,
          "type": "ENTITY"
        }
      ]
    },
    {
      "metricId": "builtin:host.cpu.usage",
      "displayName": "CPU usage %",
      "description": "Percentage of CPU time currently utilized.",
      "unit": "Percent",
      "entityType": [
        "HOST"
      ],
      "aggregationTypes": [
        "auto",
        "avg",
        "max",
        "min"
      ],
      "transformations": [
        "filter",
        "fold",
        "merge",
        "names",
        "parents"
      ],
      "defaultAggregation": {
        "type": "avg"
      },
      "dimensionDefinitions": [
        {
          "key": "dt.entity.host",
          "name": "Host",
          "index": 0,
          "type": "ENTITY"
        }
      ]
    }
  ]
}
