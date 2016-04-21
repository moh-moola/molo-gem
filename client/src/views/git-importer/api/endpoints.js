import { conj } from 'src/utils';
import { internalEndpoint } from 'src/http';


export const repos = (urlParts, opts) => endpoint(opts, {
  method: 'GET',
  url: '/import/repos/',
  params: urlParts
});


export const locales = (repoNames, opts) => endpoint(opts, {
  method: 'GET',
  url: `/import/languages/`,
  params: {repo: repoNames}
});


export const importContent = (id, locales, opts) => endpoint(opts, {
  method: 'POST',
  url: `/import/repos/${id}/import/`,
  data: {locales},
  useAuth: true
});


export const validateContent = (id, locales, opts) => endpoint(opts, {
  method: 'POST',
  url: `/import/repos/${id}/validate/`,
  data: {locales},
  useAuth: true
});


function endpoint(opts, def) {
  return internalEndpoint(conj(def, opts || {}));
}
