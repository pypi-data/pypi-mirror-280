import React from 'react';
import {
     CssBaseline,
     Typography,
     MenuItem,
     Select,
     SelectChangeEvent,
     Snackbar,
     TextField,
     Tooltip,
     styled,
     IconButton,
     InputAdornment,
     TableContainer,
     Table,
     TableBody,
     TableRow,
     TableCell,
     InputLabel,
     tableCellClasses
} from '@mui/material';
import { IoCopyOutline } from 'react-icons/io5';
import copyToSystem from '../common/copyToClipboard';
import { IEndpoint } from '../common/types';


type EndpointInfoProps = {
     endpoint: IEndpoint
}

const EndpointSummary: React.FC<EndpointInfoProps> = (props): JSX.Element => {
     const [version, setVersion] = React.useState<string>('');
     const [snackbarOpen, setSnackbarOpen] = React.useState<boolean>(false)
     const [endpointURLToCopy, setEndpointURLToCopy] = React.useState('')
     const [versionDescription, setVersionDescription] = React.useState<string>('')
     const endpointVersions = props.endpoint.versions || []

     React.useEffect(() => {
          setVersion(
               `${endpointVersions.length > 0 ? endpointVersions[0].id : ''
               }`
          );
          setVersionDescription(
               `${endpointVersions.length > 0
                    ? endpointVersions[0].description
                    : ''
               }`
          );
     }, [props.endpoint.versions]);

     React.useEffect(() => {
          setEndpointURLToCopy(
               `http://localhost:3000/endpoints/${props.endpoint.id}/versions/${version}/submit`
          );
     }, [props.endpoint.id, version]);

     const handleVersionChange = (event: SelectChangeEvent) => {
          event.preventDefault();
          console.log(event.target.value);
          setVersion(event.target.value);
          setVersionDescription(endpointVersions.find((v) => v.id === event.target.value)?.description ?? "");
     };

     const handleCopyToClipboard = () => {
          try {
               copyToSystem(endpointURLToCopy as string)
               setSnackbarOpen(true)
          } catch (error) {
               console.log(`Error copying to clipboard => ${JSON.stringify(error, null, 2)}`)
          }
     }

     const IconButtonWithTooltip = styled(IconButton)({
          root: {
               '&.Mui-disabled': {
                    pointerEvents: 'auto',
               },
          },
     });

     const AlignedInputAdornment = styled(InputAdornment)({
          margin: '0 auto', // fix for vertically unaligned icon
     });

     return (
          <React.Fragment>
               <CssBaseline />
               <TableContainer >
                    <Table sx={{
                         maxWidth: '100vw', [`& .${tableCellClasses.root}`]: {
                              borderBottom: "none"
                         }
                    }} aria-label="endpoint-info">
                         <TableBody>
                              <TableRow>
                                   <TableCell align="left">
                                        <Typography variant="body1" noWrap sx={{
                                             fontSize: '20px'
                                        }}>Notebook name:</Typography>
                                   </TableCell>
                                   <TableCell align="right" colSpan={2}>
                                        <Typography variant="body2" noWrap sx={{ fontSize: '17px' }}>{props.endpoint.notebookName}</Typography>
                                   </TableCell>
                              </TableRow>
                              <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }} >
                                   <TableCell align="left">
                                        <Typography variant="body1" noWrap sx={{ fontSize: '20px' }}>Function name:</Typography>
                                   </TableCell>
                                   <TableCell align="right" colSpan={2}>
                                        <Typography variant="body2" noWrap sx={{ fontSize: '17px' }}>{props.endpoint.functionName}</Typography>
                                   </TableCell>
                              </TableRow>
                              <TableRow sx={{ '&:last-child td, &:last-child th': { border: 0 } }} >
                                   <TableCell align="left" colSpan={2}>
                                        <InputLabel>
                                             <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>
                                                  Description of the endpoint:
                                             </Typography>
                                        </InputLabel>
                                        <TextField
                                             fullWidth
                                             variant="outlined"
                                             defaultValue={props.endpoint.description}
                                             sx={{ width: '100%' }}
                                        />
                                   </TableCell>
                              </TableRow>
                              <TableRow>
                                   <TableCell align='left'>
                                        <InputLabel id="version-select-label">
                                             <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>
                                                  Version:
                                             </Typography>
                                        </InputLabel>
                                        <Select
                                             labelId="version-select-label"
                                             id="version-select"
                                             value={version}
                                             onChange={handleVersionChange}
                                             sx={{ width: 150 }}
                                        >
                                             {(endpointVersions.length > 0) ? (
                                                  endpointVersions.map((version) => (
                                                       <MenuItem key={version.id} value={version.id}>{version.versionName}</MenuItem>
                                                  ))) : (
                                                  <MenuItem key={0} value={0}>No version</MenuItem>
                                             )}
                                        </Select>
                                   </TableCell>
                                   <TableCell sx={{ width: '100%' }}>
                                        <InputLabel>
                                             <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>
                                                  Description:
                                             </Typography>
                                        </InputLabel>
                                        <TextField
                                             disabled
                                             fullWidth
                                             variant="standard"
                                             InputProps={{
                                                  disableUnderline: true,
                                             }}
                                             multiline
                                             maxRows={2}
                                             minRows={2}
                                             value={versionDescription}
                                             sx={{ width: '100%' }}
                                        />
                                   </TableCell>
                              </TableRow>
                              <TableRow>
                                   <TableCell colSpan={2}>
                                        <InputLabel>
                                             <Typography variant='body1' noWrap sx={{ fontSize: '20px' }}>
                                                  URL:
                                             </Typography>
                                        </InputLabel>
                                        <TextField
                                             disabled
                                             variant='outlined'
                                             value={endpointURLToCopy}
                                             sx={{ width: '100%' }}
                                             InputProps={{
                                                  endAdornment: (
                                                       <AlignedInputAdornment position="end">
                                                            <Tooltip title="Copy Endpoint URL">
                                                                 <IconButtonWithTooltip role={'button'} onClick={handleCopyToClipboard}>
                                                                      <IoCopyOutline />
                                                                 </IconButtonWithTooltip>
                                                            </Tooltip>
                                                       </AlignedInputAdornment>
                                                  ),
                                             }}
                                        />
                                        <Snackbar
                                             open={snackbarOpen}
                                             onClose={() => setSnackbarOpen(false)}
                                             autoHideDuration={2000}
                                             message="Copied to clipboard"
                                        />
                                   </TableCell>
                              </TableRow>
                         </TableBody>
                    </Table>
               </TableContainer>
          </React.Fragment>
     )
};

export default EndpointSummary;
