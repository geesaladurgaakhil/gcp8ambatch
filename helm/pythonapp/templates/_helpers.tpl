{{/*
Expand the name of the chart.
*/}}

{{- define "python-app.name" -}}

{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}

{{- end }}


{{/*
Create a default fully qualified app name.
*/}}

{{- define "python-app.fullname" -}}

{{- if .Values.fullnameOverride }}

{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}

{{- else }}

{{- printf "%s-%s" .Release.Name (include "python-app.name" .) | trunc 63 | trimSuffix "-" }}

{{- end }}

{{- end }}


{{/*
Common labels
*/}}

{{- define "python-app.labels" -}}

helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}

{{ include "python-app.selectorLabels" . }}

app.kubernetes.io/managed-by: {{ .Release.Service }}

{{- end }}


{{/*
Selector labels
*/}}

{{- define "python-app.selectorLabels" -}}

app.kubernetes.io/name: {{ include "python-app.name" . }}

app.kubernetes.io/instance: {{ .Release.Name }}

{{- end }}