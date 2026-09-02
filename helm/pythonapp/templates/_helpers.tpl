{{/*
Expand the name of the chart.
*/}}

{{- define "pythonapp.name" -}}ullnameOverride

{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}

{{- end }}


{{/*
Create a default fully qualified app name.
*/}}

{{- define "pythonapp.fullname" -}}

{{- if .Values.f }}

{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}

{{- else }}

{{- printf "%s-%s" .Release.Name (include "pythonapp.name" .) | trunc 63 | trimSuffix "-" }}

{{- end }}

{{- end }}


{{/*
Common labels
*/}}

{{- define "pythonapp.labels" -}}

helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}

{{ include "pythonapp.selectorLabels" . }}

app.kubernetes.io/managed-by: {{ .Release.Service }}

{{- end }}


{{/*
Selector labels
*/}}

{{- define "pythonapp.selectorLabels" -}}

app.kubernetes.io/name: {{ include "pythonapp.name" . }}

app.kubernetes.io/instance: {{ .Release.Name }}

{{- end }}